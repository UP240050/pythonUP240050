#1.
a = int(input("Enter your age: "))
b = 18 - a
if a >= 18:
        print('You are old enough to drive.')
else:
        print("You need", b, "more years to learn to drive")
#2.
my_age = 19
your_age = int (input("Enter your age: "))
a = your_age - my_age
b = my_age - your_age
if your_age > my_age:
        print("You are", a, "older than me")
else:
        print("I am", b, "years older than you")
#3.
a = int (input("Enter one number: "))
b = int (input("Enter another number: "))
if a > b:
        print(a, "is bigger than", b)
elif a < b:
        print(a, "is smaller than", b)
else:
        print(a, "is equal to", b)


  
