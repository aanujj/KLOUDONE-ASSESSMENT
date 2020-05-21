year = int(input("enter your year: "))

if (year%400 == 0 and year%100 != 0 or year%4 == 0):
    print("The Year Is Leap Year ")


else:
     print("not a leap year")