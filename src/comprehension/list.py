import random
import timeit

TAX_RATE = 0.08
PRICES = [random.randrange(100) for _ in range(100_000)]


def get_price(price):
    return price * (1 + TAX_RATE)


def get_prices_with_map():
    # lazy evaluation
    return list(map(get_price, PRICES))


def get_prices_with_comprehension():
    return [get_price(price) for price in PRICES]


def get_prices_with_loop():
    prices = []
    for price in PRICES:
        prices.append(get_price(price))
    return prices


# Profiling with timeit, 500 times
print(timeit.timeit(get_prices_with_map, number=500))
print(timeit.timeit(get_prices_with_comprehension, number=500))
print(timeit.timeit(get_prices_with_loop, number=500))


# list comprehension
sentence = "the rocket came back from mars"
print([char for char in sentence if char in "aeiou"])
# ['e', 'o', 'e', 'a', 'e', 'a', 'o', 'a']

# list comprehension example 2
new_sentence = (
    "The rocket, who was named Ted, came back "
    "from Mars because he missed his friends."
)


def is_consonant(letter):
    vowels = "aeiou"
    return letter.isalpha() and letter.lower() not in vowels


vowel_values = [char for char in new_sentence if is_consonant(char)]
print(vowel_values)
"""
['T', 'h', 'r', 'c', 'k', 't', 'w', 'h', 'w', 's', 'n', 'm', 'd',
 'T', 'd', 'c', 'm', 'b', 'c', 'k', 'f', 'r', 'm', 'M', 'r', 's', 'b',
 'c', 's', 'h', 'm', 's', 's', 'd', 'h', 's', 'f', 'r', 'n', 'd', 's']
"""

# list comprehension example 3
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
new_price = [price if price > 0 else 0 for price in original_prices]


# [1.25, 0, 10.22, 3.78, 0, 1.16]
# equivalent to
def get_actual_price(price):
    return price if price > 0 else 0


prices = [get_actual_price(price) for price in original_prices]
print(prices)
# [1.25, 0, 10.22, 3.78, 0, 1.16]


# walrus operator from python 3.8
def get_weather_data():
    return random.randrange(90, 110)


randomTemps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
print(set(randomTemps))  # turning into a set
# [107, 102, 109, 104, 107, 109, 108, 101, 104]
