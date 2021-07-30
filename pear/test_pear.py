from pear import Pear

def t1(num1, num2):
    print('t1: ', num1 + num2)

def t2(num):
    print('t2: ', num) 

pear = Pear()
pear.add_thread(t1, [4, 5])
pear.add_thread(t2, 4)
print(pear.get_threads())
pear.remove_thread(pear.get_thread_ids()[0])
print(pear.get_threads())