from uagents import Agent, Bureau, Context, Model
observer=Agent(
    name="observer",
    port=8000,
    seed="obs",
    endpoint=["http://localhost:8000/submit"],
)#creation of ai agent responsible for observation of player
class Message(Model):
    message: str
@observer.on_message(model=Message)
async def handle_request(ctx: Context, sender: str, msg: Message):
    await ctx.send(sender, Message(message=msg.message))
if __name__ == "__main__":
    print(observer.address)
    observer.run()