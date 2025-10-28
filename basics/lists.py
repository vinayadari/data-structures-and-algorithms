users = ['Dave', 'Jhon', 'Sara']
data = ["Dave", 42, True]
emptyList = []

print("Dave" in users)  # check if the element is  in the list
print("Dave" in data)  # check if the element is  in the list
print("Dave" in emptyList)  # check if the element is  in the list

# indexing
print(users[0])
print(users[-1])
print(users[-2])

# index of value
print(users.index("Sara"))

# range of values
print(users[0:2])  # excludes the 2nd parameter
# start with specific number and then go till the last if the second element is blank
print(users[1:])
print(users[-3:-1])

# len of list
print(len(users))
print(len(data))
print(len(emptyList))

# add more items
users.append("Elsa")
print(users)

# users += "New"  # this is wrong cause it appends each character
# print(users)

users += ['Jason']
print(users)

users.extend(['Robert', 'Jimmy'])
print(users)

# users.extend(data)  # merging two lists
# print(users)

# adding to specific index
users.insert(0, 'Bob')  # index
print(users)

# slice at same position inserts the list and moves the elements to right
users[2:2] = ['Eddie', 'Alex']
print(users)

users[1:3] = ["Robert", 'Jpg']
print(users)

# removing the elements from list
users.remove('Bob')
print(users)
# remove last element
print(users.pop())
print(users)
# specific element delete
del users[0]
print(users)

# del data deleting entire list
data.clear()  # clears the list
print(data)  # empty list will be printed


users[1:1] = ['dave']
print(users)
# sorting lists
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)
