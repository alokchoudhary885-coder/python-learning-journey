# Chapter 4: Standard Library — calendar Module
# Demonstrates generating text calendars, leap year checks, and date utilities.

import calendar

# 1. Displaying Month Calendar as Text
year = 2026
month = 10
print(f"--- 1. Calendar for {calendar.month_name[month]} {year} ---")
month_str = calendar.month(year, month)
print(month_str)

# 2. Leap Year Verification
print("--- 2. Leap Year Functions ---")
print("Is 2024 a leap year? (isleap):", calendar.isleap(2024))
print("Is 2026 a leap year? (isleap):", calendar.isleap(2026))
print("Is 2000 a leap year? (isleap):", calendar.isleap(2000))
print("Is 1900 a leap year? (isleap):", calendar.isleap(1900))

# Leap years between 2000 and 2028 (exclusive of 2028)
leap_count = calendar.leapdays(2000, 2028)
print("Count of leap days between 2000 and 2028:", leap_count)

# 3. Weekday and Month Range Utilities
# weekday(year, month, day): 0 = Monday, 6 = Sunday
day_index = calendar.weekday(2026, 10, 19)
day_name = calendar.day_name[day_index]
print("\n--- 3. Day and Month Information ---")
print(f"2026-10-19 is day index {day_index} ({day_name})")

# monthrange returns (weekday_of_first_day, total_days_in_month)
first_weekday, total_days = calendar.monthrange(year, month)
print(f"October 2026 starts on weekday index {first_weekday} and has {total_days} days.")

# 4. Iterating through Day Names and Month Names
print("\n--- 4. Built-in Sequence Constants ---")
print("Weekdays :", list(calendar.day_abbr))
print("Months   :", [calendar.month_abbr[i] for i in range(1, 13)])

# 5. Using TextCalendar with Custom First Day
# By default, week starts on Monday (0). Can set Sunday (6) as first day:
custom_cal = calendar.TextCalendar(firstweekday=calendar.SUNDAY)
print("\n--- 5. Calendar Starting on Sunday ---")
print(custom_cal.formatmonth(2026, 10))
