from logging import error
from .pear_thread import PearThread
from multiprocessing import Lock

class Pear():

    locks = {}

    def __init__(self):
        self.threads = set([])
    
    def __check_race_conditions__(self):
        return False
    
    def thread_task(self , args):
        if self.get_thread_names().count(args[1].__name__) == 1:
            args[1](*(args[2]))
        else:
            args[0][args[1].__name__].acquire()
            args[1](*(args[2]))
            args[0][args[1].__name__].release()

    def get_thread_by_id(self, id):
        for thread in self.threads:
            if id is thread.get_id():
                return thread

    def is_empty(self):
        return len(self.get_threads()) == 0

    def get_threads(self):
        return self.threads

    def get_thread_names(self):
        return [thread.get_name() for thread in self.threads]

    def get_thread_ids(self):
        return [thread.get_id() for thread in self.threads]

    def add_thread(self, func, args):
        fun_arg = (self.locks , func , args)

        if not func.__name__ in self.locks.keys():
            self.locks[func.__name__] = Lock()
        
        t = PearThread(self.thread_task, fun_arg)
        t.set_name(func.__name__)
        self.threads.add(t)

    def remove_thread(self, id):
        for thread in self.threads:
            if id is thread.get_id():
                self.threads.remove(self.get_thread_by_id(id))
                return

    def run(self):
        try:
            for thread in self.threads:
                thread.start()
            for thread in self.threads:
                thread.join()
            return True
        except error:
            print(error)
            return False