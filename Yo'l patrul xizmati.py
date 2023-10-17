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


'''oka qizilga otmang!!!'''