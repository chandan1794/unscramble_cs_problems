# Time Complexity
The *Big-O* or Worst Case Scenario time complexity for the Tasks in the projects are as following:
### 1. Task0.py
`O(1)`
Searching through a Python List or slicing has the time complexity of `O(1)`.
Hence, Time Complexity of Task0 is `O(1)`.

### 2. Task1.py
```python
calls.extend(texts)
```
Extending a list: `O(n + m)`, where `n` and `m` are sizes of the lists.

```python
unique_telephone_numbers = set()
for record in calls:
    unique_telephone_numbers.add(record[0])
    unique_telephone_numbers.add(record[1])
``` 
Inserting elements in a Set: `O(1)`, 
Looping through a list: `O(n)`, where `n` is the size of the list

Both parts have linear complexity, so the final time complexity for `Task2` is `O(n)`, where `n` is
the total number of rows in both lists combined.

### 3. Task2.py
*Note: calls.txt has all data from September 2016, hence I did not introduce an explicit filter for the condition.*
Worst Case Scenario: All telephone numbers in `calls.txt`, `incoming` and `outgoing` are unique.
```python
time_per_telephone = {}
for call in calls:
    for number in [call[0], call[1]]:
        if number in time_per_telephone:
            time_per_telephone[number] = time_per_telephone[number] + int(call[-1])
        else:
            time_per_telephone[number] = int(call[-1])
```
This part of the code runs `n` times, where `n` is the number of records in calls.
Searching of the key in a dictionary has time complexity of `O(1)`.
The inner loop will always have a fixed length of two.
Hence time complexity of this part is `O(2n) => O(n)`, where `n` is the number of records in calls.

```python
max_duration = 0
max_telephone = ""
for telephone, duration in time_per_telephone.items():
    if duration > max_duration:
        max_duration = duration
        max_telephone = telephone

```
This is again just a single loop.
Hence time complexity of this part is `O(n)`, where `n` is the number of records in calls.

### 4. Task3.py
```python
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
```
Custom function to find the code, It has a constant Time Complexity, because the max length of the code is fixed.
Hence, time complexity is `O(1)`.

```python
for call in calls:
    if call[0][:5] == "(080)":
        set_telephones_from_banglore.add(find_code(call[1]))
        if call[1][:5] == "(080)":
            count_to_banglore = count_to_banglore + 1
        total_count = total_count + 1
```
Inserting in a Set: `O(1)`
For loop, iterating over all the records: `O(n)`, where `n` is the number of records in `calls.txt`
For every record, calling `find_code()` once: `O(1)`
Hence, time complexity for this part is `O(n)`.

```python
list_telephones_from_banglore = list(set_telephones_from_banglore)
list_telephones_from_banglore.sort()
for code in list_telephones_from_banglore:
    print(code)
```
Sorting a list: `O(n * log(n))`, where `n` is total number of records in `calls.txt`
Looping through a list: `O(n)`, where `n` is total number of records in `calls.txt`
Hence, final time complexity for this is `O(n * log(n))`.

Final Time Complexity for Task3 is `O(n * log(n))`.

### 5. Task4.py
```python
for call in calls:
    if call[0][:3] == "140":
        telemarketers_set.add(call[0])
```
Single loop: `O(n)`, where `n` is total number of records in `calls.txt`
Hence, final time complexity for this is `O(n)`.

```python
print("These numbers could be telemarketers: ")
list_telemarketers = list(telemarketers_set)
list_telemarketers.sort()
for telemarketer in list_telemarketers:
    print(telemarketer)
```
Sorting a list: `O(n * log(n))`, where `n` is total number of records in `calls.txt`
Looping through a list: `O(n)`, where `n` is total number of records in `calls.txt`
Hence, final time complexity for this is `O(n * log(n))`.

Final Time Complexity for Task4 is `O(n * log(n))`.