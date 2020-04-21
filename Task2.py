"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

time_per_telephone = {}
for call in calls:
    for number in [call[0], call[1]]:
        if number in time_per_telephone:
            time_per_telephone[number] = time_per_telephone[number] + int(call[-1])
        else:
            time_per_telephone[number] = int(call[-1])

max_duration = 0
max_telephone = ""
for telephone, duration in time_per_telephone.items():
    if duration > max_duration:
        max_duration = duration
        max_telephone = telephone

print(f"{max_telephone} spent the longest time, {max_duration} seconds, on the phone during September 2016")
