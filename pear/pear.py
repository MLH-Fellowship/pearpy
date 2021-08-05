import threading
from pear_thread import PearThread

class Pear():
    global lock 
    lock = threading.Lock()

    def __init__(self):
        self.threads = set([])
    
    def __check_race_conditions__(self):
        return False

    def __get_thread_by_id__(self, id):
        for thread in self.threads:
            if id is thread.get_id():
                return thread
    
    def thread_task(self,args):
        if self.get_thread_names().count(args[1].__name__) == 1:
            print(self.get_thread_names().count(args[1].__name__))
            args[1](args[2])
        else:
            args[0].acquire()
            args[1](args[2])
            args[0].release()

    def get_threads(self):
        return self.threads

    def get_thread_names(self):
        return [thread.getName() for thread in self.threads]

    def get_thread_ids(self):
        return [thread.get_id() for thread in self.threads]

    def add_thread(self, func, args):
        print(args)
        fun_arg = (lock ,func, args)
        t = PearThread(self.thread_task, fun_arg)
        t.setName(func.__name__)
        self.threads.add(t)

    def remove_thread(self, id):
        for thread in self.threads:
            if id is thread.get_id():
                self.threads.remove(self.__get_thread_by_id__(id))
                return

    def run(self):
        for thread in self.threads:
            thread.start()
        for thread in self.threads:
            thread.join()