from uagents import Agent, Bureau, Context, Model
import time, os, json
import requests
observer=Agent(
    name="observer",
    port=8000,
    seed="obs",
    endpoint=["http://localhost:8000/submit"],
)#creation of ai agent responsible for observation of player
@observer.on_event("startup")
async def starting_reputation(ctx: Context):
    ctx.storage.set("event",[])#event
    ctx.storage.set("name",[])#name
    ctx.storage.set("eva",[])#evaluation
    ctx.storage.set("rep",50)#reputation
    ctx.storage.set("number_of_events",0)
class Message(Model):
    message: str
@observer.on_message(model=Message)
async def handle_request(ctx: Context, sender: str, msg: Message):
    ctx.send(sender,Message(message=str(ctx.storage.get("reputation"))))
class Request(Model):
    text: str
class Response(Model):
    timestamp: int
    text: str
    agent_address: str

def get_fun_fact(prompt: str) -> str:
    """
    Call LLM API to get a fun fact
    """
    url = "https://api.asi1.ai/v1/chat/completions"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {os.getenv("ASI1_API_KEY")}'
    }



    payload = {
        "model": "asi1-mini",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 1.4,
        "max_tokens": 0
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']

    except requests.exceptions.RequestException as e:
        return f"API Request Error: {str(e)}"

    except json.JSONDecodeError:
        return "API Error: Unable to parse JSON response"


@observer.on_rest_post("/rest/pos", Request, Response)
async def handle_post(ctx: Context, req: Request) -> Response:
    ctx.logger.info("Received POST request")
    # req is what player says to the npc
    prompt = f"""You are a non-playable character in a computer game. You've just seen a player during an event:
{req.txt} .
You are asked to assess the behaviour of a player in terms of his reputation. 
You must respond with a name of this event and a number assessing this event in terms of reputation of the player.
The output should be a tuple of a format (str, int) where:
str - a string containing the name of the event that was described
int - one integer number between 1 and 100 which represents your assessment of the described event 
"""

    #ctx.logger.info(f"Fetching fun fact about: {topic}")
    output = get_fun_fact(prompt)
    ctx.storage.set("name",ctx.storage.get("name").append(output[0]))
    ctx.storage.set("ev",ctx.storage.get("ev").append(output[1]))
    ctx.storage.set("rep",min(100,((ctx.storage.get("rep"))*(ctx.storage.get("number_of_events")+100)+output[1])/(ctx.storage.get('number_of_events')+101)))
    ctx.storage.set('number_of_events',ctx.storage.get("number_of_events"),+1)
    return Response(
        text=f"",
        agent_address=ctx.agent.address,
        timestamp=int(time.time()),
    )
if __name__ == "__main__":
    observer.run()
    print(observer.address)