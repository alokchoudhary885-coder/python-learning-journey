# Chapter 4: Important Functions of the random Module
# Demonstrates random number generation, selections, distributions, and practical use cases.

import random

# 1. Basic Random Floats
print("--- 1. Basic Float Generation ---")
print("random() [0.0 to 1.0)      :", random.random())
print("uniform(10.0, 20.0)        :", random.uniform(10.0, 20.0))

# 2. Integer Generation
print("\n--- 2. Integer Generation ---")
print("randint(1, 100) (inclusive):", random.randint(1, 100))
print("randrange(0, 50, 5)        :", random.randrange(0, 50, 5))

# 3. Sequence Selections
fruits = ["apple", "banana", "cherry", "mango", "orange"]
print("\n--- 3. Sequence Operations ---")
print("choice(fruits)             :", random.choice(fruits))

# choices() with replacement and probability weights
weighted_choice = random.choices(
    population=["Common", "Rare", "Legendary"],
    weights=[80, 18, 2],
    k=5
)
print("choices() with weights     :", weighted_choice)

# sample() without replacement
unique_selection = random.sample(range(1, 100), 5)
print("sample(5 unique numbers)   :", unique_selection)

# shuffle() in-place
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print("shuffle(cards)             :", cards)

# 4. Reproducible Generation with seed()
print("\n--- 4. Reproducibility with seed() ---")
random.seed(123)
first_run = [random.randint(1, 50) for _ in range(4)]
random.seed(123)
second_run = [random.randint(1, 50) for _ in range(4)]
print("First run with seed 123    :", first_run)
print("Second run with seed 123   :", second_run)
print("Both runs identical?       :", first_run == second_run)

# 5. Practical Use Cases
print("\n--- 5. Practical Use Cases ---")
# 6-Digit OTP Generator
otp = "".join(str(random.randint(0, 9)) for _ in range(6))
print("Generated 6-Digit OTP      :", otp)

# Coin Toss Simulation
coin_flip = "Heads" if random.random() < 0.5 else "Tails"
print("Coin Toss Result           :", coin_flip)
