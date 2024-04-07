import timeit

"""
 https://realpython.com/list-comprehension-python/#choose-generators-for-large-datasets
"""


# in memory sum, which greedily loads the whole list into memory
def in_memory_sum():
    return sum([number * number for number in range(1000)])


print(f"Load the whole sum into memory: {in_memory_sum()}")


# lazy evaluation with less memory constraints, but slower
def lazy_sum():
    return sum(number * number for number in range(1000))


print(f"Lazy evaluation: {lazy_sum()}")

# performance comparison
# Profiling with timeit, 100_000 times
print(timeit.timeit(in_memory_sum, number=100_000))
print(timeit.timeit(lazy_sum, number=100_000))
