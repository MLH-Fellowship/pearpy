from pearpy.pear import Pear
import unittest

# Thread 1
def t1(num1, num2):
    print('t1: ', num1 + num2)

# Thread 2
def t2(num):
    print('t2: ', num)

class TestPear(unittest.TestCase):
    def __create_pear__(self):
        self.pear = Pear()

    def __init_pear__(self):
        # Add two default threads for testing
        self.pear.add_thread(t1, [4, 5])
        self.pear.add_thread(t2, 4)

    def __init_duplicate_threads__(self):
        self.pear.add_thread(t2, 1)
        self.pear.add_thread(t2, 2)

    def __reset_pear__(self):
        # Remove all threads until thread pool empty
        for i in self.pear.get_thread_ids():
            self.pear.remove_thread(i)

    def test_get_thread_by_id(self):
        self.__create_pear__()
        self.__init_pear__()
        # Check that added threads are accessible by function
        for id in self.pear.get_thread_ids():
            self.assertTrue(self.pear.get_thread_by_id(id) in self.pear.get_threads())

    def test_is_empty(self):
        self.__create_pear__()
        # Check that empty thread pool returns true, else false
        self.__reset_pear__()
        self.assertTrue(self.pear.is_empty())
        self.__init_pear__()
        self.assertFalse(self.pear.is_empty())

    def test_thread_pool(self):
        self.__create_pear__()
        self.__init_pear__()
        # Check that get_thread calls return right number of threads
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
        # Check that threads are added properly
        self.assertEqual(len(self.pear.get_threads()), 2)
        self.assertFalse(self.pear.is_empty())

    def test_remove_threads(self):
        self.__create_pear__()
        self.__init_pear__()
        self.assertFalse(self.pear.is_empty())
        # Check that thread is properly removed
        self.pear.remove_thread(self.pear.get_thread_ids()[0])
        self.assertEqual(len(self.pear.get_threads()), 1)
        # Check that invalid ID throws error
        self.assertRaises(ValueError, self.pear.remove_thread, 'INVALID_ID')
        # Check that removing last thread leaves pool empty
        self.pear.remove_thread(self.pear.get_thread_ids()[0])
        self.assertTrue(self.pear.is_empty())

    def test_run(self):
        self.__create_pear__()
        # Check that running with no threads throws error
        self.assertRaises(ValueError, self.pear.run)
        # Check that running with threads returns true
        self.__init_pear__()
        self.assertTrue(self.pear.run())
        # Check that resources are locked when duplicate threads run
        self.__reset_pear__()
        self.__init_duplicate_threads__()
        self.assertTrue(self.pear.run())


if __name__ == '__main__':
    unittest.main()
