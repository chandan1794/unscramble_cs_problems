"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
calls.extend(texts)
unique_telephone_numbers = set()
actual = 0
for record in calls:
    unique_telephone_numbers.add(record[0])
    unique_telephone_numbers.add(record[1])
    actual = actual + 2

print(f"There are {len(unique_telephone_numbers)} different telephone numbers in the records.")
print(f"Actual number of telephones {actual}")