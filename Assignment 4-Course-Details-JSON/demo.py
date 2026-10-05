import asyncio

async def hello1():
    print("Hello 1")
    await asyncio.sleep(5)
    print("World 1")

async def hello2():
    print("Hello 2")
    await asyncio.sleep(5)
    print("World 2")

async def main():
    await asyncio.gather(hello1(),hello2())
    # await hello1()
    # await hello2()

asyncio.run(main())


