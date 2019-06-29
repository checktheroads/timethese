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

tuple_set_dict = timethese.Strings(actions=(time_tuple, time_set, time_dict))
print(tuple_set_dict)
# (59.917, 286.146, 330.834)
```

You can optionally pass setup parameters with `params="a = 1"`, which will be run *per* action.

```python
import timethese

time_tuple = "len(t)"
time_set = "len(s)"
time_dict = "len(d)"

param_tuple = "t = (0,1,2,3,4,5,6,7,8,9)"
param_set = "s = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}"
param_dict = 'd = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}'

tuple_set_dict = timethese.Strings(actions=(time_tuple, time_set, time_dict), params=(param_tuple, param_set, param_dict))
print(tuple_set_dict)
# (50.301, 53.56, 50.926)
```

Lastly, you can optionally pass global parameters with `globalparams={"a": 1}`, which will be added to Python's `globals()` built in function for all actions passed:

```python
import timethese

time_tuple = "t + (to_ts,)"
time_set = "s.add(to_ts)"
time_dict = "d.update(to_d)"

param_tuple = "t = (0,1,2,3,4,5,6,7,8,9)"
param_set = "s = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}"
param_dict = 'd = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}'

tuple_set_dict = timethese.Strings(actions=(time_tuple, time_set, time_dict), params=(param_tuple, param_set, param_dict), globalparams={"to_ts": 100, "to_d": {"eleven": 11}})
print(tuple_set_dict)
# (78.568, 76.308, 150.234)
```

## License
<a href="http://www.wtfpl.net/"><img src="http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png" width="80" height="15" alt="WTFPL" /></a>
