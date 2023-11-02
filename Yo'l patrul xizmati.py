import time
from threading import Thread


def red():
    while True:
        print('Красный')
        time.sleep(10)


def yellow():
    while True:
        time.sleep(5)
        print('Жёлтый')
        time.sleep(5)


def green():
    while True:
        time.sleep(7)
        print('Зелёный')
        time.sleep(10)


hodim_red = Thread(target=red)
hodim_yellow = Thread(target=yellow)
hodim_green = Thread(target=green)
hodim_red.start()
hodim_yellow.start()
hodim_green.start()


def sync_traffic_light():
    while True:
        print("Красный")
        time.sleep(5)
        print("Желтый")
        time.sleep(2)
        print("Зеленый")
        time.sleep(5)

sync_traffic_light()


import asyncio

async def light():
    while True:
        print("Красный")
        await asyncio.sleep(5)
        print("Желтый")
        await asyncio.sleep(2)
        print("Зеленый")
        await asyncio.sleep(5)

potok = asyncio.get_event_loop()
potok.run_until_complete(light()) 



'''oka qizilga otmang!!!'''