up = int(input("enter up "))
down = int(input("enter down "))
n = up + down
if n - up > n - down:
    print(n - down)
else:
    print(n - up)
