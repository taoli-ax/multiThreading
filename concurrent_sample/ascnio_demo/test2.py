import asyncio
import time


async def test_1():
    task = asyncio.create_task(test_2())
    # 让task运行直到他完成
    # await task
    print("A")
    # 运行权交给协程，询问你有没有其他其他程序要执行，给你1秒的空余时间
    await asyncio.sleep(5)
    print("B")
    # 交给 task，跳转到test_2继续执行
    # await task


async def test_2():
    print("1")
    # 我只需要2秒就完成了任务，如果有其他任务，可以限制性其他，没有的话，就轮到我执行
    await asyncio.sleep(2)
    print("2")


asyncio.run(test_1())
