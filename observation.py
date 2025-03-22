from uagents import Agent, Bureau, Context, Model
import time, os
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

@observer.on_rest_post("/rest/post", Request, Response)
async def handle_post(ctx: Context, req: Request) -> Response:
    ctx.storage.set("event",ctx.storage.get("event").append(req.text))
    
    ctx.storage.set("number_of_events",ctx.storage.get("number_of_events")+1)
    return Response(
        text=f"",
        agent_address=ctx.agent.address,
        timestamp=int(time.time()),
    )
if __name__ == "__main__":
    observer.run()
    print(observer.address)