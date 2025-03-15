#1.
grade = float(input("Enter your grade: "))
if grade >= 80 and grade <= 100:
        print("Your grade is A")
elif grade >= 70 and grade <= 89:
        print("Your grade is B")
elif grade >= 60 and grade <= 69:
        print("Your grade is C")
elif grade >= 50 and grade <= 59:
        print("Your grade us D")
else: print("Your grade is F")

#2.
month = str (input("Enter a month: "))
A = ["september", "october", "november"]
B = ["december", "january", "february"]
C = ["march", "april", "may"]
if month in A:
        print("The season is Autom")
elif month in B:
        print("The season is Winter")
elif month in C:
        print("The season is Spring")
else: print("The season is Summer")

#3
fruits = ['banana', 'naranja', 'mango', 'limón']
nueva_fruta = input('Introduce el nombre de una fruta: ')
if nueva_fruta in fruits:
        print('Esa fruta ya está en la lista')
else:
        fruits.append(nueva_fruta)
        print('Lista modificada: ', fruits)

