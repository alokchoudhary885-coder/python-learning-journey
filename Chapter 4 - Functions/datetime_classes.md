# Important Classes of the datetime Module

## 1. Definition
The `datetime` module is built upon five primary object-oriented classes: **`date`** (calendar date), **`time`** (clock time independent of date), **`datetime`** (combined date and time), **`timedelta`** (a duration or difference between two dates/times), and **`timezone`** (a concrete timezone offset implementation).

## 2. Why We Use These Classes
- **Data Specialization:** Use `date` when time does not matter (birthdays, holidays); use `time` for schedule slots (opening hours); use `datetime` for exact timestamps.
- **Date Mathematics:** `timedelta` allows safe addition and subtraction across months, leap years, and daylight savings without manual arithmetic errors.
- **Timezone Safety:** `timezone` prevents confusion between local servers and UTC cloud systems.

## 3. Overview of Key Classes
| Class | Constructor Example | Primary Use |
|---|---|---|
| `date` | `date(2026, 10, 19)` | Year, Month, Day |
| `time` | `time(14, 30, 0)` | Hour, Minute, Second, Microsecond |
| `datetime` | `datetime(2026, 10, 19, 14, 30)` | Full calendar + clock snapshot |
| `timedelta` | `timedelta(days=7, hours=4)` | Difference or duration between dates |
| `timezone` | `timezone(timedelta(hours=5, minutes=30))` | Fixed UTC offset |

## 4. Simple Explanation: How `timedelta` Arithmetic Works
- When you subtract two `date` or `datetime` objects:
  $$\text{datetime}_2 - \text{datetime}_1 = \text{timedelta}$$
- When you add a `timedelta` to a `date` or `datetime`:
  $$\text{datetime} + \text{timedelta} = \text{new\_datetime}$$
- Python automatically adjusts day rollovers (e.g., adding 5 days to October 28 correctly lands on November 2).

## 5. Practical Example
```python
from datetime import date, datetime, timedelta

# Project deadline calculator
start_date = date.today()
duration = timedelta(weeks=2, days=3)  # 17 days
deadline = start_date + duration

print("Project Started :", start_date)
print("Deadline Date   :", deadline)
print("Days remaining  :", (deadline - start_date).days)
```

## 6. Expected Output
```text
Project Started : 2026-10-19
Deadline Date   : 2026-11-05
Days remaining  : 17
```

## 7. Important Differences: Naive vs Aware datetime
| Type | Characteristics | How to Create |
|---|---|---|
| **Naive datetime** | Has no timezone attached (`tzinfo=None`). Assumes local system clock. | `datetime.now()` |
| **Aware datetime** | Explicitly includes timezone offset (`tzinfo` specified). Safe across global servers. | `datetime.now(timezone.utc)` |

## 8. Common Mistakes
1. **Subtracting `date` from `datetime`:** Writing `datetime.now() - date.today()` raises `TypeError`. Convert with `.date()` first: `datetime.now().date() - date.today()`.
2. **Comparing Naive and Aware Datetimes:** Comparing naive and aware datetimes raises `TypeError: can't compare offset-naive and offset-aware datetimes`.
3. **Invalid Parameter Ranges:** Passing `month=13` or `day=32` raises `ValueError`.

## 9. Short Revision Notes
- `date(year, month, day)`
- `time(hour, minute, second)`
- `datetime.combine(date_obj, time_obj)` merges date and time.
- `timedelta` parameters: `days`, `seconds`, `microseconds`, `milliseconds`, `minutes`, `hours`, `weeks`.
- Use `timezone.utc` for cloud and API data.

## 10. Practice Questions with Answers

### Q1. How do you find the date 30 days from today?
**Answer:**
```python
from datetime import date, timedelta
future_date = date.today() + timedelta(days=30)
```

### Q2. How do you calculate how many days are left until New Year 2027?
**Answer:**
```python
from datetime import date
days_left = (date(2027, 1, 1) - date.today()).days
```

### Q3. Can a `timedelta` object hold a negative duration?
**Answer:** Yes. A `timedelta` can represent negative durations (e.g., when subtracting a future date from a past date or doing `now - timedelta(days=5)`).

### Q4. How do you extract just the `date` part from a `datetime` object?
**Answer:**
```python
dt = datetime.now()
d = dt.date()
```

### Q5. What is the difference between an offset-naive and an offset-aware datetime object?
**Answer:** An offset-naive object does not store timezone information (`tzinfo is None`). An offset-aware object includes a specific timezone offset (like UTC or IST), eliminating ambiguity in global time calculations.
