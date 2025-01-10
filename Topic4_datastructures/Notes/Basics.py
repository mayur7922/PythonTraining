# Learning about lists, tuples, dictionaries and sets in python

# 1) lists

arr = [3,2,5,4,1]

arr.sort()
arr.reverse()

print(len(arr))

# 2) tuples

tup = (1,2,3,4,5)

tup[0] = 10

print(tup)

# 3) dictionary

dict = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}

print(dict['b'])
print(dict.get('d'))

for item in dict:
    print(item)

for item in dict.values():
    print(item)

for item in dict.items():
    print(item)

# 4) sets

set = {5,4,3,2,1}

print(set)

for it in set:
    print(it)

# returns true
print(1 in set)

# returns false
print(7 in set)

set.add(9)
set.remove(2)

print(set)