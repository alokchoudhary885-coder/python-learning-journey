# Chapter 4: The Actual Python Import Hierarchy Demo
# =====================================================
# How Python really finds, loads, and caches modules behind the scenes.

import sys
import math

print("--- 1. sys.modules: The Module Cache ---")
# When you write 'import x', Python FIRST checks sys.modules dictionary.
# If 'x' is already present, Python returns the cached module object immediately!
print(f"Total currently loaded modules in sys.modules: {len(sys.modules)}")
print("Is 'math' in sys.modules? :", "math" in sys.modules)
print("Is 'random' in sys.modules?:", "random" in sys.modules)

# Notice what happens if we import math again:
import math as m2
print("Is re-imported math identical to original? (m2 is math):", m2 is math)


print("\n--- 2. sys.meta_path: Meta Path Finders ---")
# If the module is NOT in sys.modules, Python consults 'sys.meta_path'.
# Each finder on sys.meta_path is asked if it can handle the module.
print("Registered meta path finders in sys.meta_path:")
for index, finder in enumerate(sys.meta_path, start=1):
    print(f"  {index}. {finder}")
# Typically contains:
# 1. BuiltinImporter (for built-in C modules like sys)
# 2. FrozenImporter (for frozen modules bundled with Python)
# 3. PathFinder (searches sys.path for .py, .pyc, packages, and C extensions)


print("\n--- 3. sys.path: Locations for Path-Based Finder ---")
# The PathFinder uses sys.path list to search for user-defined and standard library files.
print("Search paths inside sys.path:")
for index, path in enumerate(sys.path[:5], start=1):
    print(f"  [{index}] {path}")
print(f"  ... and {len(sys.path) - 5} more directories.")

# Crucial observation:
# sys.path[0] is ALWAYS the directory containing the running script (or current working directory).
print(f"\nNotice: sys.path[0] is '{sys.path[0]}'")
print("Because the current directory is first, a local file named 'math.py' or 'random.py'")
print("will be found BEFORE the standard library, causing accidental module shadowing!")


print("\n--- 4. Inspecting Module __file__ Attribute ---")
# Every file-based module has a __file__ attribute pointing to its location on disk.
# Note: Built-in C modules (like 'sys') do NOT have a __file__ attribute!
print("'math' module __file__ attribute  :", getattr(math, "__file__", "Built-in (compiled in C)"))
print("'sys' module __file__ attribute   :", getattr(sys, "__file__", "Built-in (compiled in C)"))

import random
print("'random' module __file__ attribute:", random.__file__)


print("\n--- 5. sys.path_hooks and sys.path_importer_cache ---")
# When PathFinder searches a directory in sys.path, it checks sys.path_hooks
# to see if a custom importer applies (e.g., zipimport for .zip files).
# It caches the resulting finders in sys.path_importer_cache for fast repeated lookups.
print(f"Number of registered path hooks        : {len(sys.path_hooks)}")
print(f"Number of cached paths in importer cache: {len(sys.path_importer_cache)}")
