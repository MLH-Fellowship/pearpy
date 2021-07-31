# Pear
The Python package for (pear)allelizing your tasks across multiple CPU threads.

## Usage
 1. Create a `Pear()` object. This will be a wrapper for all of your multithreaded processes.
 2. Identify the functions on which you would like to paralleilze computation.
 3. Add your tasks to the Pear object. If a potential race condition is detected, an error will be thrown.
 4. Run the paraellelized processes.

## Example
```
from pear import Pear

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
```
