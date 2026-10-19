# calendar Module in Python

## 1. Definition
The **`calendar`** module is a built-in Python module that provides functions to output plain text calendars, compute calendar metadata, calculate leap years, and determine weekday indices.

## 2. Why We Use the `calendar` Module
- **Printable Schedules:** Generate formatted ASCII calendars for years or specific months without writing layout loops.
- **Leap Year Calculations:** Accurate mathematical checks for leap years (`isleap()`, `leapdays()`).
- **Date Boundary Queries:** Quickly determine the number of days in a month and what day of the week a month starts on (`monthrange()`).

## 3. Syntax
```python
import calendar

# Print month calendar string
print(calendar.month(2026, 10))

# Check leap year
is_leap = calendar.isleap(2024)

# Get weekday (0=Monday, 6=Sunday)
day_num = calendar.weekday(2026, 10, 19)

# Month range: (weekday_start, total_days)
start_day, days_in_month = calendar.monthrange(2026, 10)
```

## 4. Simple Explanation: How Weekday Numbering Works
- Python's `calendar` module follows the **ISO 8601** convention:
  - `0` $\rightarrow$ Monday
  - `1` $\rightarrow$ Tuesday
  - `2` $\rightarrow$ Wednesday
  - `3` $\rightarrow$ Thursday
  - `4` $\rightarrow$ Friday
  - `5` $\rightarrow$ Saturday
  - `6` $\rightarrow$ Sunday
- `calendar.day_name[index]` maps the integer back to the full name string.

## 5. Practical Example
```python
import calendar

# Checking total days in February for leap vs non-leap years
year1 = 2024  # Leap year
year2 = 2026  # Non-leap year

print(f"Feb {year1} days:", calendar.monthrange(year1, 2)[1])  # 29
print(f"Feb {year2} days:", calendar.monthrange(year2, 2)[1])  # 28
```

## 6. Expected Output
```text
Feb 2024 days: 29
Feb 2026 days: 28
```

## 7. Important Differences: `calendar` vs `datetime`
| Feature | `calendar` Module | `datetime` Module |
|---|---|---|
| **Focus** | Month/Year grids, visual formatting, leap logic | Individual timestamps, durations, arithmetic |
| **Output Type** | Formatted text blocks, multi-line strings | Python objects (`datetime`, `date`, `time`) |
| **Date Math** | High-level (leap counts, month ranges) | Exact second-level durations (`timedelta`) |

## 8. Common Mistakes
1. **0-indexed Weekdays:** Assuming Sunday is `0`. In Python's `calendar` and `datetime`, Monday is `0` and Sunday is `6`.
2. **Inclusive vs Exclusive `leapdays`:** `calendar.leapdays(y1, y2)` includes `y1` but excludes `y2`.
3. **Invalid Month Numbers:** Passing `month=0` or `month=13` raises `calendar.IllegalMonthError`.

## 9. Short Revision Notes
- `calendar.month(year, month)` returns a formatted month string.
- `calendar.isleap(year)` returns `True` for leap years.
- `calendar.monthrange(year, month)` returns `(first_weekday, num_days)`.
- Weekday range: `0` (Monday) to `6` (Sunday).
- Use `TextCalendar(firstweekday=...)` to customize the starting day of the week.

## 10. Practice Questions with Answers

### Q1. How do you print the full calendar for the entire year 2026?
**Answer:**
```python
import calendar
print(calendar.calendar(2026))
```

### Q2. Write a one-liner to check if the year 2000 was a leap year.
**Answer:**
```python
import calendar
print(calendar.isleap(2000))  # True
```

### Q3. What does `calendar.weekday(2026, 1, 1)` return if January 1, 2026 is a Thursday?
**Answer:** It returns `3` (since Monday=0, Tuesday=1, Wednesday=2, Thursday=3).

### Q4. How can you find how many days are in February 2028 programmatically?
**Answer:**
```python
import calendar
days = calendar.monthrange(2028, 2)[1]
# Result: 29
```

### Q5. How do you change the first day of the week to Sunday in a `TextCalendar`?
**Answer:**
```python
import calendar
cal = calendar.TextCalendar(firstweekday=calendar.SUNDAY)
```
