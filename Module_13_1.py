import asyncio


# Асинхронная функция, имитирующая участие силача в соревновании
async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")

    # Задержка, обратно пропорциональная силе
    delay = 5 / power  # Чем больше сила, тем меньше задержка

    # Подъем 5 шаров
    for i in range(1, 6):  # 1 до 5 включительно
        await asyncio.sleep(delay)  # Задержка
        print(f"Силач {name} поднял {i} шар.")

    # Завершение соревнований
    print(f"Силач {name} закончил соревнования.")


# Асинхронная функция для запуска турнира
async def start_tournament():
    # Создаем задачи для участников
    task1 = asyncio.create_task(start_strongman("Pasha", 3))
    task2 = asyncio.create_task(start_strongman("Denis", 4))
    task3 = asyncio.create_task(start_strongman("Apollon", 5))

    # Ожидаем завершения всех задач
    await asyncio.gather(task1, task2, task3)


# Запуск турнира
if __name__ == "__main__":
    asyncio.run(start_tournament())
