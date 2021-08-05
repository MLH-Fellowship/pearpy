from pear.pear import Pear
import unittest

def t1(num1, num2):
    print('t1: ', num1 + num2)

def t2(num):
    print('t2: ', num) 

class TestPear(unittest.TestCase):
    def __create_pear__(self):
        self.pear = Pear()
        
    def __init_pear__(self):
        self.pear.add_thread(t1, [4, 5])
        self.pear.add_thread(t2, 4)

    def __reset_pear__(self):
        for i in self.pear.get_thread_ids():
            self.pear.remove_thread(self.pear.get_thread_ids[i])

    def test_get_thread_by_id(self):
        self.__create_pear__()
        self.__init_pear__()
        for id in self.pear.get_thread_ids():
            self.assertTrue(self.pear.get_thread_by_id(id) in self.pear.get_threads())

    def test_is_empty(self):
        self.__create_pear__()
        self.__reset_pear__()
        self.assertTrue(self.pear.is_empty())
        self.__init_pear__()
        self.assertFalse(self.pear.is_empty())

    def test_thread_pool(self):
        self.__create_pear__()
        self.__init_pear__()
        self.assertEqual(len(self.pear.get_threads()), 2)
        self.assertEqual(len(self.pear.get_thread_names()), 2)
        self.assertEqual(len(self.pear.get_thread_ids()), 2)
        for i in range(1, 10):
            self.pear.add_thread(t1, [3, 9])
            self.assertEqual(len(self.pear.get_threads()), 2 + i)
            self.assertEqual(len(self.pear.get_thread_names()), 2 + i)
            self.assertEqual(len(self.pear.get_thread_ids()), 2 + i)

    def test_add_threads(self):
        self.__create_pear__()
        self.assertTrue(self.pear.is_empty())
        self.__init_pear__()
        self.assertEqual(len(self.pear.get_threads()), 2)
        self.assertFalse(self.pear.is_empty())

    def test_remove_threads(self):
        self.__create_pear__()
        self.__init_pear__()
        self.assertFalse(self.pear.is_empty())
        self.pear.remove_thread(self.pear.get_thread_ids()[0])
        self.assertEqual(len(self.pear.get_threads()), 1)
        self.pear.remove_thread(self.pear.get_thread_ids()[0])
        self.assertTrue(self.pear.is_empty())

    def test_run(self):
        self.__create_pear__()
        self.__init_pear__()
        self.assertTrue(self.pear.run())


if __name__ == '__main__':
    unittest.main()