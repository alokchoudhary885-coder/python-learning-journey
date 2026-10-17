# Chapter 4: reduce() Function in Python
# ========================================
# Unlike map() and filter() which are built-in functions, reduce() belongs
# to the 'functools' standard module in Python 3.
#
# Why is reduce() in functools?
# Guido van Rossum (creator of Python) moved it from built-ins to functools in Python 3
# because excessive or nested use of reduce() can make code harder to read than a clear loop.
#
# Syntax:
#     from functools import reduce
#     reduce(function, iterable[, initializer])
#
# The function must take exactly TWO arguments:
#     1. Accumulator: Stores the ongoing aggregated result.
#     2. Current element: The next item from the iterable.

from functools import reduce

# 1. Sum of all elements using reduce() with a Normal Function
def add(accumulator, current_value):
    print(f"  add({accumulator}, {current_value}) -> returns {accumulator + current_value}")
    return accumulator + current_value


numbers = [1, 2, 3, 4, 5]

print("--- 1. Step-by-Step Execution of reduce() ---")
print("Input List:", numbers)
total_sum = reduce(add, numbers)
print("Final Total Sum:", total_sum)


# 2. Product of Elements using Lambda
product = reduce(lambda acc, val: acc * val, numbers)
print("\n--- 2. Product using Lambda ---")
print("Numbers:", numbers)
print("Product (1 * 2 * 3 * 4 * 5):", product)


# 3. Finding Maximum Value using reduce()
data = [42, 17, 89, 56, 23, 91, 14]
max_value = reduce(lambda a, b: a if a > b else b, data)

print("\n--- 3. Finding Maximum Value ---")
print("Data List :", data)
print("Max Value :", max_value)


# 4. Combining Strings using reduce()
words = ["Python", "is", "powerful", "and", "fun"]
sentence = reduce(lambda acc, word: f"{acc} {word}", words)

print("\n--- 4. Combining Strings ---")
print("Words List :", words)
print("Sentence   :", sentence)


# 5. Using the Optional 'initializer' Argument
# When initializer is given, it is placed BEFORE the first item of the sequence.
base_balance = 1000
transactions = [250, -100, 500, -50]
final_balance = reduce(lambda acc, txn: acc + txn, transactions, base_balance)

print("\n--- 5. Using Initializer ---")
print("Initial Balance:", base_balance)
print("Transactions   :", transactions)
print("Final Balance  :", final_balance)


# 6. What happens with an Empty Iterable?
print("\n--- 6. Empty Iterable Behavior ---")
empty_list = []

# Case A: Empty iterable WITH an initializer returns the initializer safely:
safe_result = reduce(lambda a, b: a + b, empty_list, 0)
print("Empty list with initializer=0 ->", safe_result)

# Case B: Empty iterable WITHOUT initializer raises TypeError:
try:
    reduce(lambda a, b: a + b, empty_list)
except TypeError as error:
    print("Empty list WITHOUT initializer raises TypeError:", error)


# 7. Comparison: map() vs filter() vs reduce()
print("\n--- 7. Comparison: map() vs filter() vs reduce() ---")
sample_nums = [1, 2, 3, 4, 5, 6]

# map(): transforms every element (N -> N)
mapped = list(map(lambda x: x * 10, sample_nums))

# filter(): selects elements meeting condition (N -> <= N)
filtered = list(filter(lambda x: x % 2 == 0, sample_nums))

# reduce(): aggregates all elements into a single value (N -> 1)
reduced = reduce(lambda a, b: a + b, sample_nums)

print("Original List :", sample_nums)
print("map(* 10)     :", mapped)
print("filter(even)  :", filtered)
print("reduce(sum)   :", reduced)
