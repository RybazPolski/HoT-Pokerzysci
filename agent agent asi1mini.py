import json
import time
from typing import Dict, Any

import requests
from uagents import Agent, Context, Model
import os
from dotenv import load_dotenv

class Message(Model):
    personality: str
    background: str
    friendship: int
class intMessage(Model):
    message: int
class Request(Model):
    text: str
class Response(Model):
    timestamp: int
    text: str
    agent_address: str

NPC_stats=""
reputation=0
observer_agent_address="agent1q2zam6zs3jxshnn0jelehkkwu7ukmamldn4qy4cklt26uwtzmvqs53hsecf"
npc_agent_address="agent1qw06qla42q4vxna78ftp76d7g2j878hlvpqhkj67mdvk9g65736hzpp2vcs"
# Load environment variables
load_dotenv()

# Initialize the agent
agent = Agent(name="AI_Fun_Fact_Bot", seed="LLM agent", port=8007, endpoint=["http://localhost:8007/submit"])

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


@agent.on_event("startup")
async def generate_fun_fact(ctx: Context):
    ctx.logger.info(f"Starting...")


@agent.on_rest_get("/rest/get", Response)
async def handle_get(ctx: Context) -> Dict[str, Any]:
    ctx.logger.info("Received GET request")
    return {
        "timestamp": int(time.time()),
        "text": "Hello from the GET handler!",
        "agent_address": ctx.agent.address,
    }


@agent.on_rest_post("/rest/post", Request, Response)
#@agent.on_event("startup")
async def handle_post(ctx: Context, req: Request) -> Response:
    ctx.logger.info("Received POST request")
    # req is what player says to the npc
    global npc_agent_address
    global observer_agent_address
    await ctx.send(npc_agent_address, Message(message="statystyki"))#adres
    await ctx.send(observer_agent_address, Message(message="statystyki"))  # adres

    global NPC_stats
    global reputation
    prompt = f"""
You are a non-playable character in a computer game. Your traits are {NPC_stats[0]}. Your background is {NPC_stats[1]}. 
Your friendship level on a scale from 1 to 100 (where 50 is neutral) is {NPC_stats[2]} . 
His global reputation on a scale from 1 to 100 (where 50 is neutral) is {reputation} .
You are having a conversation with the player. The player just said to you: "{req.text}". 
What is your response? 
You must respond with words, i.e. by saying something to the player.
Furthermore, you should adjust your friendship level about the player according to your interaction.
The output should have the JSON format provided below
{
    "response":"<NPC's answer>",
    "new_friendship_level":"<Integer between 0 and 100 which represents a value of how much you like him>",
}
"""

    #ctx.logger.info(f"Fetching fun fact about: {topic}")
    output = get_fun_fact(prompt)

    ##update friendship levelu do bazy danych

    return Response(
        text=f"{output.response}",
        agent_address=ctx.agent.address,
        timestamp=int(time.time()),
    )


#used to update the statistics of our NPC from the NPC agent to the LLM agent
@agent.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    #ctx.logger.info(f"Received message from {sender}: {msg.message}")
    global NPC_stats
    NPC_stats = [msg.personality, msg.background, msg.friendship]

@agent.on_message(model=intMessage)
async def message_handler(ctx: Context, sender: str, msg: Message):
    #ctx.logger.info(f"Received message from {sender}: {msg.message}")
    global reputation
    reputation = msg.message

if __name__ == "__main__":
    #print(agent.address)
    agent.run()
