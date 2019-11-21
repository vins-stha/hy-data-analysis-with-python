def mydate(day=1, month=1):   # Generates dates starting from the given date
    lengths=(31,28,31,30,31,30,31,31,30,31,30,31)   # How many days in a month
    first_day=16
    weekdays = ("S","m","t","w","Th","Fr","sa")
    wkd  = "Fr"
    monthNow = 8
    for m in range(month, 13):
        for d in range(first_day, lengths[m-1] + 1):
            for wd in range(wkd, len(weekdays)):
                yield (wd,d, m)
        first_day=1
# Create the generator by calling the function:
gen = mydate(26, 2)   # Start from 26th of February
for i, (day, month) in enumerate(gen):
    if i == 5: break                 # Print only the first five dates from the generator
    print(f"Index {i}, day {day}, month {month}")