"""
Times the runtime of input actions, returns tuple of values in microseconds.
"""

# Standard Imports
import timeit


def Strings(actions=(None,), params=(None,), globalparams={None: None}):
    """
    Accept any number of strings for actions to execute, time each execution, convert
    each execution time to microseconds, append "usec" to each item, return tuple of all
    input run times in microseconds.
    """
    # Actions Validation
    # Handle no actions passed
    if not all(actions):
        raise AttributeError("No actions are specified")
    # Handle tuple with non-strings
    elif isinstance(actions, tuple) and not all(
        tuple(map(lambda a: isinstance(a, str), actions))
    ):
        raise TypeError("Action items must be strings")
    # Handle empty tuple
    elif isinstance(actions, tuple) and False in actions:
        raise TypeError("Action items must be strings")
    # Handle standalone string not in tuple
    elif not isinstance(actions, tuple) and isinstance(actions, str):
        actions = (actions,)
    # Handle non-tuples
    elif not isinstance(actions, tuple):
        raise TypeError("Actions must be tuples")
    #
    # Global Parameters Validation
    # Handle non-dict
    if not isinstance(globalparams, dict):
        raise TypeError("Global Parameters must be a dictionary")
    elif all(globalparams) and not all(
        tuple(map(lambda gp: isinstance(gp, str), globalparams.keys()))
    ):
        raise TypeError("Global Parameter items must be strings")
    usecs = None
    if all(params):
        #
        # Instance Parameter Validation
        # Handle standalone string not in tuple
        if isinstance(params, str):
            params = (params,)
        # Handle non-tuples
        elif not isinstance(params, tuple):
            raise TypeError("Parameters must be tuples")
        # Handle tuple with non-strings
        elif (
            isinstance(params, tuple)
            and all(globalparams)
            and not all(tuple(map(lambda a: isinstance(a, str), params)))
        ):
            raise TypeError("Parameter items must be strings")
        # Handle empty tuple
        elif isinstance(params, tuple) and len(params) == 0:
            raise TypeError("Parameters cannot be empty if passed")
        if all(globalparams):
            timer = lambda action, param: timeit.timeit(
                action, setup=param, globals=globalparams, number=1000000
            )
        elif not all(globalparams):
            timer = lambda action, param: timeit.timeit(
                action, setup=param, number=1000000
            )
        action_groups = tuple(zip(actions, params))
        usecs = ()
        for action_group in action_groups:
            usecs += (
                round(
                    timer(
                        [action for action in action_group][0],
                        [action for action in action_group][1],
                    )
                    * 1000,
                    3,
                ),
            )
    elif not all(params):
        if all(globalparams):
            timer = lambda action: timeit.timeit(
                action, globals=globalparams, number=1000000
            )
        elif not all(globalparams):
            timer = lambda action: timeit.timeit(action, number=1000000)
        usecs = ()
        for action in actions:
            usecs += (round(timer(action) * 1000, 3),)
    else:
        raise AttributeError("Error reading Instance Parameters")
    return usecs
