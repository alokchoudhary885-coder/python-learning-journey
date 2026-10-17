# reduce() Function in Python

## 1. Definition
The `reduce()` function performs rolling computations across sequential pairs of values in an iterable until only a single cumulative result remains. Unlike `map()` and `filter()`, `reduce()` produces a single scalar value from a collection of items.

## 2. Why We Use It & Why in `functools`
- **Cumulative Aggregation:** Ideal for operations that compress a sequence into a single value (such as cumulative sum, product, or state updates).
- **Why in `functools`:** In Python 2, `reduce()` was a built-in. In Python 3, Guido van Rossum moved it to the `functools` module because in most daily cases, explicit built-in functions like `sum()`, `max()`, `min()`, or a standard `for` loop are much more readable.

## 3. Syntax
```python
from functools import reduce

reduce(function, iterable[, initializer])
```
- `function`: A function accepting exactly two arguments: `(accumulator, current_item)`.
- `iterable`: The sequence to reduce.
- `initializer` *(optional)*: An initial seed value placed before the items of the sequence.

## 4. Simple Explanation of How It Works (The Accumulator Concept)
For `numbers = [1, 2, 3, 4]`:
1. Step 1: `acc = 1`, `val = 2` $\rightarrow$ `add(1, 2) = 3` (new accumulator)
2. Step 2: `acc = 3`, `val = 3` $\rightarrow$ `add(3, 3) = 6` (new accumulator)
3. Step 3: `acc = 6`, `val = 4` $\rightarrow$ `add(6, 4) = 10`
4. Result: `10`

If an `initializer` (e.g. `100`) is supplied:
- Step 1 starts with `acc = 100` and `val = 1`.

## 5. Practical Examples
```python
from functools import reduce

# 1. Product of list elements
numbers = [2, 3, 4, 5]
product = reduce(lambda acc, x: acc * x, numbers)
print("Product:", product)

# 2. Maximum value
scores = [45, 82, 19, 94, 63]
max_score = reduce(lambda a, b: a if a > b else b, scores)
print("Max Score:", max_score)

# 3. Concatenating words with custom separator
words = ["Learn", "Python", "Step", "By", "Step"]
joined = reduce(lambda a, b: f"{a} -> {b}", words)
print("Joined:", joined)
```

## 6. Expected Output
```text
Product: 120
Max Score: 94
Joined: Learn -> Python -> Step -> By -> Step
```

## 7. Important Differences: `map()` vs `filter()` vs `reduce()`
| Feature | `map()` | `filter()` | `reduce()` |
|---|---|---|---|
| **Module** | Built-in | Built-in | `functools` |
| **Input $\rightarrow$ Output** | $N \rightarrow N$ items | $N \rightarrow \le N$ items | $N \rightarrow 1$ item |
| **Function signature** | 1 argument (or per iterable) | 1 argument (returns boolean) | Exactly 2 arguments |
| **Output Type** | Iterator (`map` object) | Iterator (`filter` object) | Single value |

## 8. Common Mistakes
1. **Forgetting to import `reduce`:** Calling `reduce(...)` directly raises `NameError: name 'reduce' is not defined`. Always include `from functools import reduce`.
2. **Empty iterable without initializer:** Calling `reduce(func, [])` raises `TypeError: reduce() of empty iterable with no initial value`. Always provide an initializer when the collection could be empty.
3. **Function with wrong parameter count:** Passing a function with 1 or 3 parameters causes `TypeError`.

## 9. Short Revision Notes
- `reduce()` boils down an iterable to a single value.
- Must import from `functools`.
- Takes a binary function (2 parameters).
- Initializer prevents `TypeError` on empty sequences and acts as the starting value.
- When built-ins like `sum()` or `math.prod()` exist, prefer them over `reduce()` for readability.

## 10. Practice Questions with Answers

### Q1. How do you import `reduce()` in Python 3?
**Answer:**
```python
from functools import reduce
```

### Q2. What happens if you call `reduce(lambda a, b: a + b, [])` without an initializer?
**Answer:** It raises `TypeError: reduce() of empty iterable with no initial value`.

### Q3. Write a `reduce()` expression to calculate the factorial of 5 using a range `[1, 2, 3, 4, 5]`.
**Answer:**
```python
from functools import reduce
fact_5 = reduce(lambda a, b: a * b, range(1, 6))
# Result: 120
```

### Q4. Write a `reduce()` statement to find the longest string in `["cat", "elephant", "dog", "hippopotamus"]`.
**Answer:**
```python
animals = ["cat", "elephant", "dog", "hippopotamus"]
longest = reduce(lambda a, b: a if len(a) > len(b) else b, animals)
# Result: 'hippopotamus'
```

### Q5. Explain how the accumulator works in `reduce(lambda acc, x: acc + x, [10, 20, 30], 5)`.
**Answer:**
- Initializer is `5`, so Step 1: `acc = 5`, `x = 10` $\rightarrow$ `15`.
- Step 2: `acc = 15`, `x = 20` $\rightarrow$ `35`.
- Step 3: `acc = 35`, `x = 30` $\rightarrow$ `65`.
- Final result: `65`.
