a = []
b = []
c = []
for i in range(int(input())):
    a.append(int(input()))
print(a)
for j in range(int(input())):
    b.append(int(input()))
print(b)
for k in a:
    if k in b and k not in c:
        c.append(k)
print(sorted(c))