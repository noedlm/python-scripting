# get word with the least characters
string = "bitcoin take over the world maybe who knows perhaps"
print(min(string.split(" "), key=len))

# reverse loop
for i in range(8,-8,-1):
    print(i)

# dictionaries and keys
filled_dict = {"one": 1, "two": 2, "three": 3}

it = filled_dict.keys()
print(it) # dict_keys(['one', 'two', 'three'])
print(list(filled_dict.keys())) # ['one', 'two', 'three']

array_sides = [1,2,3,4,3,2,1]

def sides(arr):
    for i in range(0, len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i

    return -1

print(sides(array_sides))

'''
Description: Next biggest number with the same digits.
Ex: 12 => 21
Ex: 13215664 => 13216456
Ex: 13215964 => 13216459

TODO: need to check the number that's
 '''


nbn = list(str(13215964))
index = -1

for i in range(len(nbn)-1, 0, -1):
    if nbn[i] > nbn[i-1]:
        nbn = nbn[:i-1] + sorted(nbn[i-1:len(nbn)], reverse=True)
        nbn = nbn[:i] + sorted(nbn[i:len(nbn)])
        index = i
        break

print(''.join(nbn))



nbn[index] = nbn[index+1]

print(nbn)

print(index)

print(''.join(sorted(list(nbn[i:]))))

import math
print(math.floor(39/10))

x = 39
li = list(str(x))
result = 1
for i in range(0, len(li)):
    result *= int(li[i])

print(result)