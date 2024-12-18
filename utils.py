import time
from dataclasses import dataclass
from functools import wraps
import sys


@dataclass(frozen=True)
class P2d:
    x: int
    y: int

    def __add__(self, other):
        return P2d(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar: int):
        return P2d(scalar * self.x, scalar * self.y)

    def __rmul__(self, scalar: int):
        return self * scalar  # Reuse the __mul__ method

    def __sub__(self, other):
        return (-1 * other) + self

    def __neg__(self):
        return P2d(-self.x, -self.y)

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y


DOWN = P2d(1, 0)
UP = P2d(-1, 0)
RIGHT = P2d(0, 1)
LEFT = P2d(0, -1)


def print_grid(grid):
    min_x, *_, max_x = sorted(p.x for p in grid)
    min_y, *_, max_y = sorted(p.y for p in grid)

    for i in range(min_x, max_x + 1):
        for j in range(min_y, max_y + 1):
            print(grid.get(P2d(i, j)), end="")
        print()


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


if __name__ == "__main__":
    p = P2d(0, 0)
    p1 = p + P2d(1, 1)
    print(p1)
    p2 = 2 * P2d(2, 5)
    print(p2)
    p3 = p2 - p1
    print(p3)
