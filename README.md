[![Build](https://github.com/MLH-Fellowship/pod-3.1.4-team-2/actions/workflows/build.yml/badge.svg)](https://github.com/MLH-Fellowship/pod-3.1.4-team-2/actions/workflows/build.yml)
[![PyPI version](https://img.shields.io/pypi/v/pearpy)](https://pypi.org/project/pearpy/)

# Pearpy
The Python package for (pear)allelizing your tasks across multiple CPU threads.

## Installation
The latest version of Pearpy can be installed with:
```
pip install pearpy
```
To stay up to date with Pearpy's releases, visit the [official page](https://pypi.org/project/pearpy/) on PyPi!

## Usage
 1. Create a `Pear()` object. This will be a wrapper for all of your multithreaded processes.
 2. Identify the functions on which you would like to paralleilze computation.
 3. Add your tasks to the Pear object. If a potential race condition is detected, an error will be thrown.
 4. Run the paraellelized processes.

## Example
```
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
```

## Race Condition Handling
When multiple threads utilize the same function, Pear will automatically generate locks for each resource. This allows developers to utilize Pear's multithreading without having to worry about inaccurate data caused by race conditions. The following example shows how race conditions are handled:
```
from pearpy.pear import Pear

global_var = 10

# This function reads from and writes to a global variable
def t_duplicated(num):
    global global_var
    print('t_duplicated: ', num + global_var)
    global_var += 1

# Pear object created with two threads accessing a shared resource
# A race condition is detected and locks are generated
pear = Pear()
pear.add_thread(t_duplicated, 1) # This should return 11 because 1 + 10 = 11
pear.add_thread(t_duplicated, 1) # This should return 12 because global_var is incremented
pear.run()

##########
# OUTPUT #
##########
t_duplicated: 11
t_duplicated: 12
```

## Benchmarks and Tests
Benchmarks can be examined via the `make benchmark` command. This will display the threaded vs unthreaded runtimes on a set script, along with the percent improvement between the two. Here is an example of what the benchmarks should look like:
```
----------------------------------------------------------------------
THREADED BENCHMARK
3.8507602214813232 s
----------------------------------------------------------------------
UNTHREADED BENCHMARK
13.90523624420166 s
----------------------------------------------------------------------
Improvement:  361.1036638072611 %
.
----------------------------------------------------------------------
Ran 1 test in 17.757s

OK
```
To run tests, utilize the `make test` command. This will output the results of the functions called in the `/tests/test_pear.py` script, along with the status of the tests themselves. The console will display 'OK' if the tests are passing.

## Contributing
Pear is open source and contributions from anyone are welcome. To contribute to this project, please submit issues and pull requests via GitHub. In order to successfully merge a pull request, all unit tests must be passed when run via `make test`. Thank you!
