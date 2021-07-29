import threading

class Pear():
    def __init__(self, num_threads=0):
        self.num_threads = num_threads
        self.threads = []
    
    def __check_race_conditions__(self):
        return False

    def add_thread(self, func, args):
        self.threads.append(threading.Thread(target=func, args=(args)))

    def run(self):
        for thread in self.threads:
            thread.start()
        for thread in self.threads:
            thread.join()