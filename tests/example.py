from pearpy.pear import Pear

# First function to be parallelized
def t1(num1, num2):
    print('t1: ', num1 + num2)

# Second function to be paralellized
def t2(num):
    print('t2: ', num) 

# Create pear object, add threads, and run
pear = Pear()
pear.add_thread(t1, [4, 5])
pear.add_thread(t2, 4)
pear.run()
