# Chapter 4: map() Function in Python
# ====================================
# The map() built-in function applies a specified function to every item
# of an iterable (like a list or tuple) and returns an iterator (a map object).
#
# Syntax:
#     map(function, iterable, ...)

# 1. Using map() with a Normal (def) Function
def square(number):
    """Returns the square of a number."""
    return number * number


numbers = [1, 2, 3, 4, 5]

# map() applies square() to every element of numbers
squared_iterator = map(square, numbers)

# The result is a map object (an iterator), convert it to a list:
squared_numbers = list(squared_iterator)

print("--- 1. map() with Normal Function ---")
print("Original Numbers:", numbers)
print("Squared Numbers :", squared_numbers)


# 2. Using map() with a Lambda Function
# Useful for quick, one-off transformations without defining a separate function.
doubled_numbers = list(map(lambda x: x * 2, numbers))

print("\n--- 2. map() with Lambda Function ---")
print("Doubled Numbers :", doubled_numbers)


# 3. Using map() with Strings
# Example A: Converting strings to uppercase
names = ["alok", "rahul", "priya", "amit"]
uppercase_names = list(map(str.upper, names))

print("\n--- 3. map() with Strings ---")
print("Original Names :", names)
print("Uppercase Names:", uppercase_names)

# Example B: Parsing string inputs to integers (very common in coding problems)
numeric_strings = ["10", "25", "40", "85"]
parsed_integers = list(map(int, numeric_strings))
print("Parsed Integers:", parsed_integers)


# 4. Using map() with Multiple Iterables
# When passing multiple iterables, the function must accept that many arguments.
# map() stops when the shortest iterable is exhausted.
list1 = [10, 20, 30]
list2 = [1, 2, 3]

sums = list(map(lambda a, b: a + b, list1, list2))

print("\n--- 4. map() with Multiple Iterables ---")
print("List 1:", list1)
print("List 2:", list2)
print("Sum of pairs:", sums)


# 5. Comparing map() vs Traditional for-loop
def square_with_loop(nums):
    result = []
    for n in nums:
        result.append(n * n)
    return result


print("\n--- 5. Comparison with for-loop ---")
loop_result = square_with_loop(numbers)
map_result = list(map(lambda n: n * n, numbers))
print("Loop Result :", loop_result)
print("Map Result  :", map_result)
print("Do they produce identical results?:", loop_result == map_result)


# 6. Practice Questions with Solutions
print("\n--- 6. Practice Questions Solutions ---")

# Question 1: Convert temperatures from Celsius to Fahrenheit using map()
# Formula: (C * 9/5) + 32
celsius_temps = [0, 20, 37, 100]
fahrenheit_temps = list(map(lambda c: (c * 9 / 5) + 32, celsius_temps))
print("Q1 (Celsius to Fahrenheit):", fahrenheit_temps)

# Question 2: Find lengths of words in a sentence
words = ["Python", "Learning", "Journey", "Functions", "Map"]
word_lengths = list(map(len, words))
print("Q2 (Word Lengths):", word_lengths)

# Question 3: Add corresponding elements of three lists
a = [1, 2, 3]
b = [10, 20, 30]
c = [100, 200, 300]
three_sum = list(map(lambda x, y, z: x + y + z, a, b, c))
print("Q3 (Three List Sum):", three_sum)

# Question 4: Capitalize each word in a list
fruits = ["apple", "banana", "cherry"]
capitalized_fruits = list(map(str.capitalize, fruits))
print("Q4 (Capitalized):", capitalized_fruits)

# Question 5: Round a list of float prices to 2 decimal places
raw_prices = [19.992, 5.456, 120.301, 45.789]
rounded_prices = list(map(lambda p: round(p, 2), raw_prices))
print("Q5 (Rounded Prices):", rounded_prices)
