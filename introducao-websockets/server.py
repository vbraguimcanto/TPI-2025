import asyncio
import websockets

async def handler(websocket):
    print("Cliente conectado.")
    async for message in websocket:
        print(f"Mensagem recebida: {message}")
        await websocket.send(f"Echo: {message}")

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("Servidor rodando em ws://localhost:8765")
        await asyncio.Future()  

asyncio.run(main())
