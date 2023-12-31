# import time
# import threading

# global running

# def perform():
#     global running

#     counter = 0
#     running = True
#     while running:
#         print('counter:', str(counter))
#         time.sleep(2)
#         counter += 1

# my_thread = threading.Thread(target=perform)
# my_thread.setDaemon(True)
# my_thread.start()

# # python 3
# input("Press Enter to stop…")

# # python 2
# #raw_input("Press Enter to stop…")

# running = False
# my_thread.join(2)

# OR

import time
import threading


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = False

    def run(self):
        counter = 0
        self.running = True
        while self.running:
            print('counter:', str(counter))
            time.sleep(2)
            counter += 1

    def stop(self):
        print('stopping thread…')
        self.running = False
        self.join(2)


my_thread = MyThread()
my_thread.setDaemon(True)
my_thread.start()

# python 3
input("Press Enter to stop…")

# python 2
# raw_input("Press Enter to stop…")
my_thread.stop()
