import websocket, os, threading, json, asyncio

os.system("title MW Onliner")
os.system("cls")

c = 0

async def online(token, t):
    global c
    try:
        token = token.split(":")[2]
    except:
        token = token
    ws = websocket.WebSocket()
    ws.connect("wss://gateway.discord.gg/?v=6&encoding=json")
    ws.send(json.dumps(
    {
    "op": 2,
    "d": {
        "token": token,
        "properties": {
            "$browser": "Yas",
            }
        }
    }
    ))
    print(f"[T{t}] Token Onlined! - {token}ㅣMW Onliner")
    c += 1

async def run(token, t):
    await asyncio.gather(online(token, t))
        

t = 0
for token in open("tokens.txt", "r").read().split("\n"):
    t += 1
    threading.Thread(target=asyncio.run, args=(run(token, t),)).start()
while True:
    if c == len(open("tokens.txt", "r").read().split("\n")):
        break

os.system("pause")