"""
Times the runtime of input actions, returns tuple of values in microseconds.
"""

# Standard Imports
import timeit


def Strings(*actions, setup=None):
    """Accept any number of strings for actions to execute, time each execution, convert each \
    execution time to microseconds, append "usec" to each item, return tuple of all input run \
    times in microseconds."""
    for action in actions:
        if not isinstance(action, str):
            raise TypeError("Action must be a string")
    if setup:
        timer = lambda action: timeit.timeit(
            action, setup, globals=globals(), number=1000000
        )
    if not setup:
        timer = lambda action: timeit.timeit(action, globals=globals(), number=1000000)
    msecs = tuple(timer(action) for action in actions)
    usec = lambda msec: round(msec * 1000, 3)
    usecs = tuple(usec(msec) for msec in msecs)
    return usecs
