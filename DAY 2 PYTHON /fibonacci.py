n = int(input("How Many numbers you want : "))

a= 0
b= 1

for i in range(n):
    print(a)
    new = a
    a = b
    b = new + a

print(b)


