# map() Function in Python

## 1. Definition
The `map()` function is a built-in higher-order function in Python that takes a function and an iterable (such as a list, tuple, or string) as arguments. It applies the function to every single element of the iterable and returns an iterator (a `map` object).

## 2. Why We Use It
- **Code Conciseness:** Eliminates the need to write multi-line `for` loops and boilerplate `.append()` calls for transforming data.
- **Memory Efficiency:** Returns a lazy iterator that generates items on demand instead of loading everything into memory at once.
- **Expressive Transformations:** Makes data transformations (like parsing strings to numbers or normalizing text) clean and readable.

## 3. Syntax
```python
map(function, iterable, ...)
```
- `function`: The function to apply to each element (can be a standard `def` function, a `lambda`, or a built-in function like `int`, `len`, `str.upper`).
- `iterable`: One or more iterables (lists, tuples, sets, strings).

## 4. Simple Explanation of How It Works
1. `map()` takes the first element from the iterable and feeds it to the specified function.
2. The function computes the result and `map()` yields that value.
3. It repeats this step for every subsequent element until the iterable is exhausted.
4. If multiple iterables are provided, `map()` takes one element from each iterable simultaneously and stops when the shortest iterable ends.

## 5. Practical Examples
```python
# Example 1: With a normal function
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

temps_c = [0, 25, 100]
temps_f = list(map(celsius_to_fahrenheit, temps_c))
print("Fahrenheit:", temps_f)

# Example 2: With a lambda function
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)

# Example 3: Multiple iterables
list1 = [10, 20, 30]
list2 = [1, 2, 3]
totals = list(map(lambda a, b: a + b, list1, list2))
print("Sums:", totals)
```

## 6. Expected Output
```text
Fahrenheit: [32.0, 77.0, 212.0]
Squares: [1, 4, 9, 16]
Sums: [11, 22, 33]
```

## 7. Important Differences from Related Concepts
| Feature | `map()` | `filter()` | Normal `for` Loop |
|---|---|---|---|
| **Purpose** | Transforms every item | Selects items matching condition | General-purpose iteration |
| **Output Size** | Same length as input iterable | Less than or equal to input length | Flexible |
| **Return Type** | Lazy `map` object | Lazy `filter` object | Whatever is constructed |
| **Efficiency** | Implemented in C, memory efficient | Implemented in C, memory efficient | Interpreted Python loop |

## 8. Common Mistakes
1. **Forgetting to convert the map object:** Writing `print(map(square, nums))` prints `<map object at 0x...>` instead of values. Wrap it in `list(map(...))`.
2. **Passing function call instead of reference:** Writing `map(square(x), nums)` instead of `map(square, nums)`.
3. **Mismatched arguments with multiple iterables:** If passing two lists to `map()`, the mapping function must accept two arguments.

## 9. Short Revision Notes
- `map()` transforms data: $N$ inputs $\rightarrow$ $N$ outputs.
- In Python 3, `map()` returns an iterator, not a list.
- Passing `str.upper` or `int` directly as the function argument is clean and idiomatic.
- When multiple iterables have different lengths, `map()` stops at the shortest one.

## 10. Practice Questions with Answers

### Q1. How do you convert a list of strings `["1", "2", "3"]` into integers using `map()`?
**Answer:**
```python
str_nums = ["1", "2", "3"]
int_nums = list(map(int, str_nums))
# Result: [1, 2, 3]
```

### Q2. What does `map()` return in Python 3 if you do not cast it to a list?
**Answer:** It returns a lazy `map` object (an iterator), not a list.

### Q3. Write a `map()` statement to find the length of each word in `["Apple", "Banana", "Cherry"]`.
**Answer:**
```python
fruits = ["Apple", "Banana", "Cherry"]
lengths = list(map(len, fruits))
# Result: [5, 6, 6]
```

### Q4. Given two lists `[1, 2, 3]` and `[4, 5]`, what will `list(map(lambda x, y: x * y, [1, 2, 3], [4, 5]))` produce?
**Answer:** `[4, 10]`. It stops at the shortest list length (2 elements).

### Q5. Convert a list of prices `[100, 250, 400]` to prices with 18% GST added using `map()`.
**Answer:**
```python
prices = [100, 250, 400]
prices_with_gst = list(map(lambda p: round(p * 1.18, 2), prices))
# Result: [118.0, 295.0, 472.0]
```
