# timethese
timethese is a blatantly lazy abstration of the standard library `timeit.timeit()` function, which runs a particular Python command x number of times in one second, and returns the result. Mainly used by me to test and learn the performance differences of various operations, but with less typing.

## Installation

```console
$ pip3 install git+https://github.com/checktheroads/timethese.git
```

## Usage
```python
import timethese

time_tuple = "t = (0,1,2,3,4,5,6,7,8,9); len(t)"
time_set = "s = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}; len(s)"
time_dict = 'd = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}; len(d)'

tuple_set_dict = timethese.Strings(time_tuple, time_set, time_dict)
print(tuple_set_dict)
# (62.068, 260.607, 332.321)
```

## License
<a href="http://www.wtfpl.net/"><img src="http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png" width="80" height="15" alt="WTFPL" /></a>
