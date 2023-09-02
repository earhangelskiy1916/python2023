p = int(input("enter p "))
s = int(input("enter s "))
d = s * s - 4 * p
n1 = (s + d ** (1.0 / 2)) / 2
n2 = (s - d ** (1.0 / 2)) / 2
print(int(n1), int(n2))
