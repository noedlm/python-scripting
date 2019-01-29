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

arr = [1,2,3,4,5,6,3,2,5,6,3,2,4,5,3,2,5,5,3,2,4,4]
print(dict.fromkeys(reversed(arr)))
print(list(reversed(list(dict.fromkeys(reversed(arr))))))
alist = []
print(reversed(alist))
for i in reversed(alist):
    print(i)

print(alist)
re = 'abc'
print(re[-1])
