import multiprocessing
import uuid

class PearThread(multiprocessing.Process):
    def __init__(self, func, args):
        super().__init__(target=func, args=(args if (type(args) is list) else [args]))
        self.id = uuid.uuid4().int & (1<<16)-1

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name