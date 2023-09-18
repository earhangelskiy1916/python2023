l = []
first_nubmer = int(input("enter first nubmer: "))
step = int(input("enter step: "))
for i in range(int(input("enter length: "))):
    l.append(first_nubmer + i * step)
print(l)