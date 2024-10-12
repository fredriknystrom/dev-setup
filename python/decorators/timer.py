import time
from functools import wraps

def timer(func):
    """
    A decorator that measures and prints the execution time of a function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time  # Calculate the elapsed time
        print(f"Function '{func.__name__}' executed in {elapsed_time:.3f} seconds")
        return result  # Return the result of the function
    return wrapper

# Example usage of the timer decorator

@timer
def example_usage(seconds):
    """
    Function that simulates a task by sleeping for the given number of seconds.
    """
    time.sleep(seconds)

# Calling the function to see the decorator in action
example_usage(3)
