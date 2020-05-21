number = int(input("enter your num greater than one "))

for i in range(2,number):
    if number%i ==0:
        print("it is not prime number ")
        break
    else:
        print("prime prime number ")