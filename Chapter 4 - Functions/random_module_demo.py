# Chapter 4: Standard Library Demo — random Module
# ====================================================
# The 'random' module implements pseudo-random number generators for various distributions.
# It is part of the standard library (ships with Python).

import random

print("--- 1. Generating Random Floats ---")
# random() returns a random float in the range [0.0, 1.0)
print("Random float between 0.0 and 1.0:", random.random())

# uniform(a, b) returns a random float between a and b
print("Random float between 10.5 and 20.5:", random.uniform(10.5, 20.5))

print("\n--- 2. Generating Random Integers ---")
# randint(a, b) returns a random integer N such that a <= N <= b (inclusive)
dice_roll = random.randint(1, 6)
print("Simulating a 6-sided dice roll:", dice_roll)

# randrange(start, stop, step)
random_even = random.randrange(2, 21, 2)
print("Random even integer between 2 and 20:", random_even)

print("\n--- 3. Random Selection from a Sequence ---")
colors = ["Red", "Blue", "Green", "Yellow", "Purple"]
picked_color = random.choice(colors)
print("Available colors:", colors)
print("Randomly chosen color:", picked_color)

print("\n--- 4. Random Sampling without Replacement ---")
# sample(population, k) picks k unique items
lottery_numbers = range(1, 50)
winning_ticket = random.sample(lottery_numbers, 5)
print("5 Lucky numbers from 1 to 49:", winning_ticket)

print("\n--- 5. Shuffling a Sequence In-Place ---")
cards = ["Ace", "King", "Queen", "Jack", "10"]
print("Cards before shuffle:", cards)
random.shuffle(cards)
print("Cards after shuffle :", cards)

print("\n--- 6. Setting a Seed for Reproducibility ---")
# Setting a seed guarantees the same sequence of numbers across runs (crucial in ML/testing)
random.seed(42)
val1 = random.randint(1, 100)
random.seed(42)
val2 = random.randint(1, 100)
print("First call with seed 42 :", val1)
print("Second call with seed 42:", val2)
print("Are they identical?      :", val1 == val2)
