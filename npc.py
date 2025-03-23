from uagents import Agent, Bureau, Context, Model
import random
Personality=[
    "Argumentative",
"Arrogant",
"Blustering",
"Rude",
"Curious",
"Friendly",
"Honest",
"Hot tempered",
"Irritable",
"Ponderous",
"Quiet",
"Suspicious",
]
Adam=Agent(
    name="Adam",
    port=8001,
    seed="Adam",
    endpoint=["http://localhost:8001/submit"],
)#creation of ai agent responsible for NPC character
@Adam.on_event("startup")
async def starting_stats(ctx: Context):
    a=random.randint(0,11)
    b=a
    c=a
    while b==a:
        b=random.randint(0,11)
    while c==a or c==b:
        c=random.randint(0,11)
    ctx.storage.set("personality1",Personality[a])
    ctx.storage.set("personality2",Personality[b])
    ctx.storage.set("personality3",Personality[c])
    ctx.storage.set("background","")
    ctx.storage.set("friendship",50)
    ctx.storage.set("interactions",0)
class Message(Model):
    personality: str
    background: str
    friendship:str
class mess(Model):
    messsege:str
@Adam.on_message(model=mess)
async def statystyki_llm(ctx: Context, sender: str, msg: mess):
    if sender=="agent1qfjj6yve05fleykn6dp29q6pz75nra8p9gs62j2eg926gagfpyxgxvd30au":
        if msg.message=="statystyki":
            await ctx.send("agent1qfjj6yve05fleykn6dp29q6pz75nra8p9gs62j2eg926gagfpyxgxvd30au", Message(personality=ctx.storage.get("Personality1")+" "+ctx.storage.get("Personality3")+" "+ctx.storage.get("Personality2"),background=ctx.storage.get("background"),friendship=ctx.storage.get("friendship")))
        else:
            ctx.storage.set("friendshipness",max(100,((ctx.storage.get("friendshipness")*(100+ctx.storage.get("interactions")))+int(msg.message))/(101+ctx.storage.get("interactions"))))
            
if __name__ == "__main__":
    Adam.run()
    print(Adam.address)