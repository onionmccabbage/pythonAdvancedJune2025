import asyncio

async def handleRequests(reader, writer):
    data = await reader.read(1024)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print(f'Received {message} from {addr}')
    writer.close()

async def main():
    server = await asyncio.start_server(handleRequests, 'localhost', 8989)
    print('server started')
    async with server:
        await server.serve_forever()

if __name__ == '__name__':
    asyncio.run( main() )
