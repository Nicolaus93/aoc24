import time
from functools import wraps
import sys


def measure_runtime(func):
    """
    A decorator to measure the runtime of a function using perf_counter.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  # Start the timer
        result = func(*args, **kwargs)   # Call the actual function
        end_time = time.perf_counter()  # End the timer
        runtime = end_time - start_time
        print(f"Function '{func.__name__}' took {runtime:.6f} seconds to complete.")
        return result
    return wrapper


def progressbar(it, size=60, out=sys.stdout):
    count = len(it)
    start_time = time.perf_counter()

    def show(j):
        current_time = time.perf_counter()
        elapsed_time = current_time - start_time

        x = int(size * j / count)
        print(
            f"[{u'█' * x}{('.' * (size - x))}] {j}/{count} ({elapsed_time:.1f}s) ",
            end="\r",
            file=out,
            flush=True,
        )
        return

    show(0.1)  # avoid div/0
    for i, item in enumerate(it):
        yield item
        show(i + 1)
    print("\n", flush=True, file=out)
