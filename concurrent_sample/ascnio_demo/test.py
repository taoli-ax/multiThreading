import asyncio


async def test_1():
    print("A")
    # 交给 test_2
    await test_2()
    print("B")


async def test_2():
    print("1")
    await asyncio.sleep(2)
    print("2")


asyncio.run(test_1())
