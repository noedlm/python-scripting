def ror(string, size):
    if (size <= 0 or len(string) == 0) or (size > len(string)):
        return ""
    


# just trying things down here

sl = [16,26,36,46,56,66]
n = "123456789846546213"
size = 8
i = 0

while i+size < len(n):
    sub = n[i:i+size]
    for c in sub:
        print(int(c)**3)
    i += size

for i in range(len(n)):
    if i > len(n):    
        break

    sub = n[i:i+size]
    i += size
    print(i)
    print(sub)


empty_string = ""
print(len(empty_string))

print(n[0:5])

print(len(sl)-1)

for s in range(len(sl)):
    print(s)
    print(sl[s])

print(len(sl))

def f(list):
    return list

sl.remove(sl[0])
print(sl)
ts = f(sl)
print(ts)
print(10%2)

print(((1**2)+(2**2))**(1/2.0))