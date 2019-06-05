import threading
from threading import Thread
from time import sleep

from multiprocessing import Process

def f(x):
    while True:
        print(x)
        sleep(1)

if __name__ == "__main__":
    server = Process(target=f)
    server.start()
    input('unesi nesto: ')
    server.terminate()
    server.join()
    print('kraj')