l = []
lmin = int(input("enter min value: "))
lmax = int(input("enter max value: "))
for i in range(int(input("enter length: "))):
    l.append(int(input("enter numbers: ")))
for j in range(len(l)):
    if l[j] >= lmin and l[j] <= lmax:
        print(j, end = " ")