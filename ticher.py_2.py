import time
import asyncio
async def get_temp():
    print("Первое показание")
    await asyncio.sleep(2)
    print("25 C")

async def get_pres():
    print("Второе показание")
    await asyncio.sleep(4)
    print("101 kPa")

async def main():
    print("Старт")
    task_1 = asyncio.create_task(get_temp())
    task_2 = asyncio.create_task(get_pres())
    await asyncio.gather(task_1, task_2)
    print("Финиш")

start = time.time()
asyncio.run(main())
finish = time.time()

print(f"Времея рабоы = {round(finish-start, 2)} сек")