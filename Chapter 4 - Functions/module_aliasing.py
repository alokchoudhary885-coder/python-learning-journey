# Chapter 4: Module Aliasing in Python
# ======================================
# Aliasing allows you to give an imported module or function an alternative,
# usually shorter or more descriptive, name using the 'as' keyword.

# 1. Standard Module Aliasing
# Syntax: import module_name as alias_name
import math as m
import random as rd

print("--- 1. Standard Module Aliasing ---")
print("math.sqrt(49) using 'm.sqrt(49)'   :", m.sqrt(49))
print("math.pi using 'm.pi'                :", m.pi)
print("random.randint(1, 10) using 'rd'    :", rd.randint(1, 10))


# 2. Function Aliasing via Import
# Syntax: from module_name import function_name as alias_name
from math import sqrt as square_root, factorial as fact

print("\n--- 2. Function Aliasing via Import ---")
print("Square root of 81 using 'square_root':", square_root(81))
print("Factorial of 5 using 'fact'          :", fact(5))


# 3. Difference: Module Aliasing vs Function Aliasing in Python
# Module Aliasing (Import-time):
#     import math as m
#     Binds the module object to the identifier 'm' in current namespace.
#
# Function Aliasing (Runtime assignment):
#     def add(a, b): return a + b
#     plus = add
#     Assigns the existing function object to a new variable name in memory.

def multiply(a, b):
    return a * b

# Runtime function alias:
times = multiply

print("\n--- 3. Module Aliasing vs Runtime Function Aliasing ---")
print("Runtime function alias times(6, 7):", times(6, 7))
print("Are times and multiply identical? :", times is multiply)


# 4. Industry Standard Aliasing Conventions
# In the Python data science ecosystem, standard community aliases are universally used:
# - import numpy as np
# - import pandas as pd
# - import matplotlib.pyplot as plt
# - import seaborn as sns
print("\n--- 4. Industry Standard Aliasing Conventions ---")
print("Standard conventions make code instantly recognizable across teams:")
print("  np  -> numpy")
print("  pd  -> pandas")
print("  plt -> matplotlib.pyplot")


# 5. Best Practices & When Aliasing Becomes an Anti-Pattern
# GOOD:
# - Shortening long package paths: 'import xml.etree.ElementTree as ET'
# - Resolving name collisions:
#   from module_a import parse as parse_a
#   from module_b import parse as parse_b
#
# BAD:
# - Cryptic single-letter aliases that confuse readers:
#   import math as x  # Poor readability!
# - Non-standard aliases for popular libraries:
#   import pandas as pan  # Violates community convention
