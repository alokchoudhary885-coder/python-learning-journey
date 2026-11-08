# Exception Handling in Python: The Complete Guide

## 1. Definition
An **Exception** is an event or error that occurs during the runtime execution of a syntactically correct Python program and disrupts its normal instruction flow.

**Exception Handling** is a programming mechanism using `try`, `except`, `else`, and `finally` blocks that allows a program to detect, intercept, and gracefully handle runtime errors rather than crashing abruptly.

---

## 2. Why We Use Exception Handling
- **Crash Prevention (Graceful Degradation):** Prevents programs from terminating unexpectedly when encountering invalid user inputs, missing files, or network drops.
- **Clean Resource Management:** Guarantees that open file handles, database connections, and network sockets are properly closed via `finally`.
- **Informative Error Messages:** Provides user-friendly feedback instead of confusing raw tracebacks.

---

## 3. Syntax & Complete Execution Flow

```python
try:
    # 1. Code that might raise an exception
    critical_operation()
except SpecificError as err:
    # 2. Runs ONLY IF SpecificError occurs inside 'try'
    handle_error(err)
else:
    # 3. Runs ONLY IF NO exception was raised in 'try'
    operation_succeeded()
finally:
    # 4. ALWAYS runs, no matter what (even on error, break, or return)
    cleanup_resources()
```

---

## 4. The Python Exception Hierarchy

All built-in exceptions in Python form an inheritance hierarchy rooted at `BaseException`:

```text
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 └── Exception (Root for all standard errors)
      ├── ArithmeticError
      │    ├── ZeroDivisionError
      │    └── OverflowError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── ValueError
      ├── TypeError
      ├── FileNotFoundError / OSError
      └── NameError
```

> [!NOTE]
> Always inherit custom exceptions from `Exception`, not `BaseException`.

---

## 5. Catching Multiple Specific Exceptions

You can catch different exception types individually or group them in a tuple:

```python
try:
    val = int(raw_input)
    result = 100 / val
except ValueError:
    print("Please enter a valid integer!")
except ZeroDivisionError:
    print("Cannot divide 100 by zero!")
except (KeyError, IndexError) as err:
    print(f"Data lookup failed: {err}")
```

---

## 6. The `raise` Keyword & Custom Exceptions

### Raising Built-in Exceptions:
```python
if balance < withdrawal:
    raise ValueError("Withdrawal exceeds balance!")
```

### Creating Custom User-Defined Exceptions:
To define domain-specific errors (e.g. `InvalidCouponError`, `AuthenticationFailedError`), subclass `Exception`:

```python
class InsufficientFundsError(Exception):
    """Raised when a bank account has insufficient balance."""
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"Cannot withdraw {amount} from balance {balance}")
    return balance - amount
```

---

## 7. Comparison: `else` vs `finally`

| Clause | When Does It Run? | Common Use Case |
| :--- | :--- | :--- |
| **`else`** | Executes **only if** the `try` block ran without raising any exception. | Code that should run only upon successful completion of the `try` block. |
| **`finally`** | Executes **always**, regardless of whether an exception occurred, was caught, or if a `return` was called. | Closing files, shutting down database connections, releasing locks. |

---

## 8. Common Mistakes
1. **Using Bare `except:` without specifying an error type:**
   ```python
   # ❌ Bad Practice: Catches KeyboardInterrupt (Ctrl+C) and SystemExit!
   try:
       do_work()
   except:
       pass
   # ✅ Pythonic Practice: Catch specific exceptions or 'except Exception:'
   try:
       do_work()
   except Exception as err:
       log_error(err)
   ```
2. **Placing broad exception handlers before specific ones:**
   If `except Exception:` is written above `except ValueError:`, the `ValueError` block will never execute because `Exception` catches it first.
3. **Suppressing errors silently (`pass` in `except`):**
   Hiding errors makes bugs nearly impossible to debug. At minimum, log or print the error.

---

## 9. Quick Revision Notes
- `try`: Wrap risky code.
- `except`: Catch and handle errors.
- `else`: Runs on complete success.
- `finally`: Guaranteed cleanup code.
- `raise`: Manually throw an exception.
- Custom exceptions inherit from `class MyError(Exception):`.

---

## 10. Practice Questions & Answers

### Q1: Does the `finally` block execute if there is a `return` statement inside `try`?
**Answer:** Yes! In Python, even if a `try` or `except` block encounters a `return` statement, the `finally` block is guaranteed to execute before the function actually exits.

### Q2: What is the output of the following code?
```python
try:
    print(10 / 2)
except ZeroDivisionError:
    print("Zero error")
else:
    print("All good")
finally:
    print("Done")
```
**Answer:**
```text
5.0
All good
Done
```

### Q3: Why is catching `BaseException` generally discouraged?
**Answer:** Because `BaseException` catches system-level signals like `KeyboardInterrupt` (when the user presses `Ctrl+C` to stop the script) and `SystemExit`, preventing the user from stopping a frozen script.

### Q4: How do you access the string description of an exception?
**Answer:** Using the `as` alias:
```python
except ValueError as err:
    print(f"Error message: {err}")
```

### Q5: Write a function `safe_divide(a, b)` that returns `None` and prints an alert on division by zero:
```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Alert: Division by zero attempted!")
        return None
```
