from pear.pear import Pear
import unittest
import random
import time

ITERATIONS = 100000000
INCREMENT = 2

def t1(num, inc):
    sum = 0
    for i in range(num):
        sum += inc
    return sum

def t2(num, inc):
    sum = 0
    for i in range(num):
        sum -= inc
    return sum

def t3(num, inc):
    sum = 0
    for i in range(num):
        sum *= inc
    return sum

def t4(num, inc):
    sum = 0
    if inc == 0: inc += random.randint(1, 100)
    for i in range(num):
        sum /= inc
    return sum

class TestPear(unittest.TestCase):
    def __create_pear__(self):
        self.pear = Pear()
        
    def __init_pear__(self):
        self.pear.add_thread(t1, [ITERATIONS, INCREMENT])
        self.pear.add_thread(t2, [ITERATIONS, INCREMENT])
        self.pear.add_thread(t3, [ITERATIONS, INCREMENT])
        self.pear.add_thread(t4, [ITERATIONS, INCREMENT])

    def test_unthreaded(self):
        start = time.time()
        print("----------------------------------------------------------------------")
        print("UNTHREADED BENCHMARK")
        t1(ITERATIONS, INCREMENT)
        t2(ITERATIONS, INCREMENT)
        t3(ITERATIONS, INCREMENT)
        t4(ITERATIONS, INCREMENT)
        end = time.time()
        print(end - start, "s")
        

    def test_threaded(self):
        start = time.time()
        self.__create_pear__()
        self.__init_pear__()
        print("----------------------------------------------------------------------")
        print("THREADED BENCHMARK")
        self.pear.run()
        end = time.time()
        print(end - start, "s")


if __name__ == '__main__':
    unittest.main()