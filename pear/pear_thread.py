import threading
import uuid

class PearThread(threading.Thread):
    def __init__(self, func, args):
        super().__init__(target=func, args=(args if (type(args) is list) else [args]))
        self.id = uuid.uuid4().int & (1<<16)-1

    def get_id(self):
        return self.id