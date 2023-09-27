import sys
users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptylist = []

print("Dave" in emptylist)
print("Dave" in users)
print("Dave" in data)

print(users[0])
print(users[-1])

print(users.index('Sara'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

# inserting element/s at the end of a list
users.append('Elsa')
print(users)

users += ['Jason']
print(users)

users.extend(['Robert', 'Jimmy'])
print(users)

# users.extend(data)
# print(users)

# inserting at an index location
users.insert(0, 'Bob')
print(users)

users[2:2] = ['Eddie', 'Alex']
print(users)


# replacing elements
users[1:3] = ['Robert', 'JPJ']
print(users)

# removing element from a list
users.remove('Bob')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()  # this empties the list
print(data)

users[1:2] = ['dave']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)


nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

# sort the list for an individual purpose and leave the original list intact
print(sorted(nums, reverse=True))
print(nums)


# three ways of making a copy of a list
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)

# Tuples (immutable data type)

mytuple = tuple(('Dave', 42, True))

anothertuple = (1, 4, 2, 8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

# creative way of updating a tuple even though it is immutable
newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)  # packing a tuple
print(newtuple)


(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))
print(anothertuple[1])
