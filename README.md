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

## Benchmarks
Benchmarks can be examined via the `make benchmark` command. This will display the threaded vs unthreaded runtimes on a set script, along with the percent improvement between the two. Here is an example of what the benchmarks should look like:
```
----------------------------------------------------------------------
THREADED BENCHMARK
6.8490447998046875 s
----------------------------------------------------------------------
UNTHREADED BENCHMARK
17.631988286972046 s
----------------------------------------------------------------------
Improvement:  257.4371872625925 %
.
----------------------------------------------------------------------
Ran 1 test in 24.481s

OK
```

## Contributing
Pear is open source and contributions from anyone are welcome. To contribute to this project, please submit issues and pull requests via GitHub. In order to successfullly merge a pull request, all unit tests must be passed when run via `make test`. Thank you!