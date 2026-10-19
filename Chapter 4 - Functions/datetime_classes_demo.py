# Chapter 4: Important Classes of datetime Module
# Explores date, time, datetime, timedelta, and timezone classes.

from datetime import date, time, datetime, timedelta, timezone

# 1. date Class (Year, Month, Day)
today = date.today()
birth_date = date(2003, 5, 15)

print("--- 1. date Class ---")
print("Today's date   :", today)
print("Specific date  :", birth_date)
print(f"ISO format     : {today.isoformat()}")

# 2. time Class (Hour, Minute, Second, Microsecond)
meeting_time = time(10, 30, 0)
lunch_break = time(13, 0)

print("\n--- 2. time Class ---")
print("Meeting scheduled for:", meeting_time)
print(f"Time components: {meeting_time.hour}h {meeting_time.minute}m")

# 3. datetime Class (Combined Date + Time)
appointment = datetime(2026, 10, 25, 11, 45, 0)
print("\n--- 3. datetime Class ---")
print("Combined appointment:", appointment)
print("Extracted date part :", appointment.date())
print("Extracted time part :", appointment.time())

# 4. timedelta Class (Durations & Date Arithmetic)
now = datetime.now()
ten_days_later = now + timedelta(days=10)
three_hours_ago = now - timedelta(hours=3)

# Calculating difference between two dates
days_lived = today - birth_date

print("\n--- 4. timedelta Class & Date Math ---")
print("Current time     :", now.strftime("%Y-%m-%d %H:%M"))
print("10 days later    :", ten_days_later.strftime("%Y-%m-%d %H:%M"))
print("3 hours ago      :", three_hours_ago.strftime("%Y-%m-%d %H:%M"))
print(f"Days since {birth_date}: {days_lived.days} days")

# 5. timezone Class (Timezone Awareness)
# Naive vs Aware datetime:
# Naive has no tzinfo; Aware has explicit timezone attached.
utc_now = datetime.now(timezone.utc)
ist_offset = timezone(timedelta(hours=5, minutes=30))
ist_now = datetime.now(ist_offset)

print("\n--- 5. timezone Class (UTC & Offsets) ---")
print("UTC time (Aware):", utc_now)
print("IST time (Aware):", ist_now)
