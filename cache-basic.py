import time


def compute(a, b):
    time.sleep(2)
    return a + b


cache = {}


def cache_compute(a, b):
    if (a, b) in cache.keys():
        return cache[a, b]
    else:
        new = compute(a, b)
        cache[a, b] = new
        return new


print(cache_compute(1, 2))
print(cache_compute(3, 5))
print(cache_compute(3, 5))
print(cache_compute(6, 7))
print(cache_compute(1, 2))
