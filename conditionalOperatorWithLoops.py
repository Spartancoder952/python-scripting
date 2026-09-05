cpu_usage = 75

if cpu_usage > 80:
    print("CRITICAL")
elif cpu_usage >=60:
    print("warning")
else:
    print("NORMAL")