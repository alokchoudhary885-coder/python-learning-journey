# datetime Module in Python

## 1. Definition
The **`datetime`** module is a Python standard library module that supplies classes for manipulating dates, times, and timestamps. It supports arithmetic on dates, parsing strings to datetime objects, and formatting datetimes into readable strings.

## 2. Why We Use the `datetime` Module
- **System Date/Time Access:** Fetch accurate local or UTC date and time.
- **Conversion & Formatting:** Convert raw text from databases or APIs into real date objects, and vice versa.
- **Timestamp Tracking:** Record creation, modification, or logging timestamps for applications.

## 3. Syntax
```python
from datetime import datetime

# Current time
now = datetime.now()

# Format object -> string
formatted_str = now.strftime("%Y-%m-%d %H:%M:%S")

# Parse string -> object
parsed_obj = datetime.strptime("2026-10-19", "%Y-%m-%d")
```

## 4. Key Formatting Codes (`strftime` & `strptime`)
| Directive | Meaning | Example |
|---|---|---|
| `%Y` | 4-digit Year | `2026` |
| `%y` | 2-digit Year | `26` |
| `%m` | Month (01 to 12) | `10` |
| `%B` | Full Month Name | `October` |
| `%b` | Short Month Name | `Oct` |
| `%d` | Day of Month (01 to 31) | `19` |
| `%A` | Full Weekday Name | `Monday` |
| `%a` | Short Weekday Name | `Mon` |
| `%H` | Hour (24-hour, 00 to 23) | `14` |
| `%I` | Hour (12-hour, 01 to 12) | `02` |
| `%M` | Minute (00 to 59) | `30` |
| `%S` | Second (00 to 59) | `45` |
| `%p` | AM or PM | `PM` |

## 5. Practical Example
```python
from datetime import datetime

# Logging timestamp pattern
log_time = datetime.now()
timestamp_str = log_time.strftime("[%Y-%m-%d %H:%M:%S]")
print(f"{timestamp_str} Server started successfully.")
```

## 6. Expected Output
```text
[2026-10-19 23:50:00] Server started successfully.
```

## 7. Important Differences: `strftime()` vs `strptime()`
| Method | Direction | Meaning | Mnemonic |
|---|---|---|---|
| `strftime()` | `datetime` object $\rightarrow$ `str` | **Str**ing **F**ormat **Time** | "f" for format |
| `strptime()` | `str` $\rightarrow$ `datetime` object | **Str**ing **P**arse **Time** | "p" for parse |

## 8. Common Mistakes
1. **Confusing `%m` and `%M`:** `%m` is 2-digit month; `%M` is minute.
2. **Confusing `%y` and `%Y`:** `%y` is 2-digit year (e.g. `26`); `%Y` is 4-digit year (e.g. `2026`).
3. **Mismatched Format in `strptime`:** If the pattern does not match the string exactly, Python raises `ValueError: time data '...' does not match format '...'`.

## 9. Short Revision Notes
- `datetime.now()` returns local datetime.
- `strftime()` converts `datetime` to string.
- `strptime()` parses string to `datetime`.
- `.timestamp()` returns floating-point seconds since Unix epoch (Jan 1, 1970).

## 10. Practice Questions with Answers

### Q1. How do you print today's date in `DD-MM-YYYY` format?
**Answer:**
```python
from datetime import datetime
print(datetime.now().strftime("%d-%m-%Y"))
```

### Q2. What error occurs if `strptime()` receives a string with a different date separator than specified in the format?
**Answer:** It raises `ValueError` stating that the data does not match the format.

### Q3. Write a code snippet to parse `"15/08/1947"` into a datetime object.
**Answer:**
```python
from datetime import datetime
dt = datetime.strptime("15/08/1947", "%d/%m/%Y")
```

### Q4. What is the difference between `%B` and `%b`?
**Answer:** `%B` gives the full month name (e.g., `October`), while `%b` gives the abbreviated 3-letter month name (e.g., `Oct`).

### Q5. How do you convert a Unix epoch timestamp (e.g., `1700000000`) into a readable datetime object?
**Answer:**
```python
from datetime import datetime
dt = datetime.fromtimestamp(1700000000)
```
