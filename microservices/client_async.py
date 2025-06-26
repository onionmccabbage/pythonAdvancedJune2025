import asyncio

async def myClient(message='default'):
    reader, writer = await asyncio.open_connection('localhost', 8989)
    print('sending message')
    writer.write(message.encode())
    await writer.drain() # wait for all the message stream to be consumed
    writer.close()

if __name__ == '__main__':
    asyncio.run( myClient('hello from asyncronous client') )