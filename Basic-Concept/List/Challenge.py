#Question 1: Reverse List in python
data = [1,2,3,4]
reverse_data = data[::-1]
print(reverse_data) #output: [4, 3, 2, 1]

def reverse_list(somevalue):
    return somevalue[::-1] 

print(reverse_list([2,4,6])) #output: [6, 4, 2]

#Question 2: find duplicates
list_data = [1,2,3,4,3,4,5]
dup_value = set(list_data)
print(dup_value) #output: {1, 2, 3, 4, 5} but the data type is set

def find_duplicate(valtwo):
    seen = set()
    duplicate = set()
    for item in valtwo:
        if item in seen:
            duplicate.add(item)
        else:
            seen.add(item)
    return list[duplicate]

print(find_duplicate([1,2,3,4,3,4,5,6])) #output: list[{3, 4}]

#Question 3: Flatten a Nested List
def flatten_list(data):
    flat_data = []
    for item in data:
        if isinstance(item, list):
            flat_data.extend(flatten_list(item))
        else:
            flat_data.append(item)
    return flat_data

print(flatten_list([12,13,14,[12,2,13,[12,14]]])) #output: [12, 13, 14, 12, 2, 13, 12, 14]

#sorted in python
words = ["apple", "banana", "kiwi", "cherry"]
words.sort(key=len)
print(words)  # Output: ['kiwi', 'apple', 'cherry', 'banana']

words = ["apple", "banana", "kiwi", "cherry"]
words.sort(key=lambda x: x[-1])  # Sort by the last character
print(words)  # Output: ['banana', 'apple', 'kiwi', 'cherry']
