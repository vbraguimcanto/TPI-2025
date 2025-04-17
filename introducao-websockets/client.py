import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            msg = input("Digite a mensagem para o servidor (ou 'sair' para encerrar): ")
            if msg.lower() == 'sair':
                print("Encerrando conexão.")
                break

            await websocket.send(msg)
            print(f"Enviado: {msg}")

            resposta = await websocket.recv()
            print(f"Recebido: {resposta}")

asyncio.run(hello())
