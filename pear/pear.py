from logging import error
from .pear_thread import PearThread

class Pear():
    def __init__(self):
        self.threads = set([])
    
    def __check_race_conditions__(self):
        return False

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
        t = PearThread(func, args)
        t.set_name(func.__name__ + '(' + str(args) + ')')
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