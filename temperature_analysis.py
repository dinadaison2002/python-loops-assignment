# Name: Dina daison
# Roll Number: IITP_AIMLTIN_2602652
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

# Assume first value as highest and lowest
highest = temperatures[0]
lowest = temperatures[0]

# Check each temperature
for temp in temperatures:
    if temp > highest:
        highest = temp
    if temp < lowest:
        lowest = temp

print("Highest Temperature:", highest, "°C")
print("Lowest Temperature:", lowest, "°C")


print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

hot_days = 0

for temp in temperatures:
    if temp <= 30:
        continue   # skip not hot days
    hot_days += 1

print("Hot Days (>30°C):", hot_days)


print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]

hot_days = 0

for day in range(len(temperatures)):
    temp = temperatures[day]

    if temp >= 40:
        print("Hot Days before alert:", hot_days)
        print("Alert! Extreme temperature", temp, "°C detected on Day", day + 1)
        break

    if temp > 30:
        hot_days += 1