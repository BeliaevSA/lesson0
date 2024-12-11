import asyncio

async def start_strongman(name, power):
    count = 0
    print(f'Силач {name} начал соревнования.')
    while count < 5:
        count += 1
        print(f'Силач {name} поднял {count} шар')
        await asyncio.sleep(1 / power)
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task_strongman1 = asyncio.create_task(start_strongman('Pasha', 3))
    task_strongman2 = asyncio.create_task(start_strongman('Denis', 4))
    task_strongman3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task_strongman1
    await task_strongman2
    await task_strongman3


asyncio.run(start_tournament())