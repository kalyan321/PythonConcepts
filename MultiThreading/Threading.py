import threading
import time


def thread1_example():
    print(threading.currentThread().getName(), 'Starting')
    for i in range(3):
        time.sleep(0.1)
        print('thread1')


def thread2_example():
    print(threading.currentThread().getName(), 'Starting')
    for i in range(3):
        time.sleep(0.1)
        print('thread2')


threading.Thread(target=thread1_example).start()
threading.Thread(target=thread2_example).start()
