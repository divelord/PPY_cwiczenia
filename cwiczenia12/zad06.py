"""
ZAD06

Utwórz menedżer kontekstu Timer, który mierzy i wypisuje czas wykonania bloku kodu.

Wywołanie
    time.perf_counter_ns()
zwraca bieżący czas z wysoką precyzją (w nanosekundach, gdzie 1s = 10^9ns).
"""
import time


class Timer:
    success = True

    def __enter__(self):
        Timer.success = True
        self.start = time.perf_counter_ns()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            Timer.success = False

            if issubclass(exc_type, ValueError):
                print("ValueError, N negative! No result")
                return True
            return False

        end = time.perf_counter_ns()
        duration = end - self.start

        print(f"Time: {duration} ns ", end="")

        return False


def fibo(n):
    if n < 0:
        raise ValueError
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


for n in (38, -1, 42, 12, 45, -9, 20):
    print(f"N = {n:2d} ", end="")

    with Timer():
        res = fibo(n)

    if Timer.success:
        print(f"res = {res:>10d}")
