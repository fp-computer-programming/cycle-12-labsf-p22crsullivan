# Author: CRS 02/23/22
# Create dictionary
grades = {"End S1 Labs": 100, "Start S2 Labs": 100, "Cycle 10 Labs": 0, "Mid-year Project Proposal": 0, "Cycle 10 Practice Quiz": 100, "Cycle 10 Quiz": 48}
print(grades.values())
# Create for loop to determine what gets printed
for v in grades:
    print(v)
for k, v in grades:
    if v == 100:
        print(k)
