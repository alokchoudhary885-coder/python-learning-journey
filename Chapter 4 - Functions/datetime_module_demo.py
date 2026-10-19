# Chapter 4: Standard Library — datetime Module Overview & Formatting
# Demonstrates getting current time, string formatting (strftime), and parsing (strptime).

from datetime import datetime, date, time
import time as system_time

# 1. Current Date and Time
now = datetime.now()
print("--- 1. Current Date and Time ---")
print("Current datetime:", now)
print(f"Components: Year={now.year}, Month={now.month}, Day={now.day}")
print(f"Time: {now.hour}:{now.minute}:{now.second}")

# 2. Formatting datetime to String (strftime)
# %Y: Year (4 digits), %m: Month (2 digits), %d: Day (2 digits)
# %H: Hour (24-hour), %M: Minute, %S: Second, %A: Weekday, %B: Month name
formatted_standard = now.strftime("%Y-%m-%d %H:%M:%S")
formatted_human = now.strftime("%A, %d %B %Y at %I:%M %p")

print("\n--- 2. Formatting with strftime() ---")
print("Standard format:", formatted_standard)
print("Readable format:", formatted_human)

# 3. Parsing String into datetime Object (strptime)
date_string = "2026-10-19 14:30:00"
parsed_dt = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

print("\n--- 3. Parsing with strptime() ---")
print("Original string  :", date_string)
print("Parsed object    :", parsed_dt)
print("Type after parse :", type(parsed_dt))

# 4. Working with UNIX Timestamps
current_epoch = now.timestamp()
converted_back = datetime.fromtimestamp(current_epoch)

print("\n--- 4. Epoch Timestamps ---")
print("Current timestamp (seconds since 1970):", current_epoch)
print("Converted back from timestamp        :", converted_back)
