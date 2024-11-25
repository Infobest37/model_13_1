import asyncio
ball = 5

# Асинхронная функция, имитирующая участие силача в соревновании
async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")

    # Задержка, обратно пропорциональная силе
    delay = ball / power  # Чем больше сила, тем меньше задержка

    # Подъем 5 шаров
    for i in range(ball):  # 1 до 5 включительно
        await asyncio.sleep(delay)  # Задержка
        print(f"Силач {name} поднял {i + 1} шар.")
    await asyncio.sleep(delay)
    print(f"Силач {name} закончил соревнования.")



# Асинхронная функция для запуска турнира
async def start_tournament():
    # Создаем задачи для участников
    task1 = asyncio.create_task(start_strongman("Pasha", 3))
    task2 = asyncio.create_task(start_strongman("Denis", 4))
    task3 = asyncio.create_task(start_strongman("Apollon", 5))

    # Ожидаем завершения всех задач
    await task1
    await task2
    await task3

    # Завершение соревнований


# Запуск турнира
asyncio.run(start_tournament())
