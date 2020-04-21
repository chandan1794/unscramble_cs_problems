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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def find_code(telephone_number):
    print(telephone_number)
    _code_ = ""
    if telephone_number[0] == "(":
        for ch in telephone_number[1:]:
            if ch == ")":
                return _code_
            _code_ = _code_ + ch
    elif telephone_number[:3] == "140":
        return "140"
    else:
        return telephone_number[:5]


set_telephones_from_banglore = set()
count_to_banglore = 0
total_count = 0

for call in calls:
    if call[0][:5] == "(080)":
        set_telephones_from_banglore.add(find_code(call[1]))
        if call[1][:5] == "(080)":
            count_to_banglore = count_to_banglore + 1
        total_count = total_count + 1

print(f"\n{'#'*10} Task A {'#'*10}")
print("The numbers called by people in Bangalore have codes:")
list_telephones_from_banglore = list(set_telephones_from_banglore)
list_telephones_from_banglore.sort()
for code in list_telephones_from_banglore:
    print(code)

print(f"\n{'#'*10} Task B {'#'*10}")
print(f"{count_to_banglore*100/total_count} percent of calls from fixed lines in Bangalore are calls to other fixed "
      f"lines in Bangalore.")
