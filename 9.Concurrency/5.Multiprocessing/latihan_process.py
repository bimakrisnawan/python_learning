import time
import multiprocessing

class MyProcess(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)
        self.running = multiprocessing.Event()  # Use Event to control process

    def run(self):
        counter = 0
        self.running.set()  # Set the event to True initially
        while self.running.is_set():
            print('counter:', str(counter))
            time.sleep(2)
            counter += 1
            
    def stop(self):
        print('stopping process…')
        self.running.clear()
        self.join()


if __name__ == '__main__':
    my_process = MyProcess()
    my_process.daemon = True
    my_process.start()

    # Wait for user input to stop
    input("Press Enter to stop…")

    my_process.stop()

    # this code is different
