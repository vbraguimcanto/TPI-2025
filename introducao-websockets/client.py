import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        msg = "Olá, servidor!"
        await websocket.send(msg)
        print(f"Enviado: {msg}")

        resposta = await websocket.recv()
        print(f"Recebido: {resposta}")

asyncio.run(hello())
