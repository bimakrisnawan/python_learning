import time
import multiprocessing


class MyProcess(multiprocessing.Process):
    def __init__(self, name, shared_data, stop_event):
        super().__init__()
        self.name = name
        self.shared_data = shared_data
        self.stop_event = stop_event

    def run(self):
        while not self.stop_event.is_set():
            time.sleep(1)
            with self.shared_data.get_lock():
                self.shared_data.value += 1
                print('Value:', self.shared_data.value, ' from ', self.name)

        print('Stopping ', self.name)


shared_data = multiprocessing.Value('i', 0, lock=True)
stop_event = multiprocessing.Event()

my_process1 = MyProcess('Process 1', shared_data, stop_event)
my_process1.daemon = True
my_process2 = MyProcess('Process 2', shared_data, stop_event)
my_process2.daemon = True

my_process1.start()
my_process2.start()

# Allow the processes to run for a while
time.sleep(5)

# Set the stop event to gracefully stop the processes
stop_event.set()

# Wait for the processes to finish
my_process1.join()
my_process2.join()
