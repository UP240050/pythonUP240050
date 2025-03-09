#1. 
a = "Thirty"
b = "Days"
c = "Of"
d = "Python"
space = " "
fin = a + space + b + space + c + space + d
print(fin)
#2. 
A = "Coding"
B = "For"
C = "All"
Space = " "
T = A + Space + B + Space + C
print (T)
#3.
company = "Coding For All"
#4. 
print(company)
#5. 
print(len("company"))
#6. 
print(company.upper ())
print(company.lower())
#7. 
print(company.capitalize())
print(company.title())
print(company.swapcase())
#8.
for_all = company[7:14] 
print(for_all) 
#9.
cut1_palabra= company.split(' ', 1)[1]
print(cut1_palabra)
#10. 
print(company.find("Coding"))
#11.
print(company.replace('Coding', 'Python')) 
#12. 
py= "Python For Everyone"
print(py.replace("Everyone", "All"))
#13.
print(company.split())
#14.
apps="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(apps.split())
#15. 
ind0= company[0]
print(ind0)
#16.
last=company[-3:]
print(last)
#17.
ind10= company[10]
print(ind10) 
#18. Python for everyone
print(py[0], py[7], py[11])
abreviacion= py[0]+py[7]+py[11]
print(abreviacion)
#19.
print(company[0], company[7], company[11])
acronimo= company[0]+company[7]+company[11]
print(acronimo)
#20.
print(company.index("C"))
#21.
print(company.index("F"))
#22.
print(company.rfind("l"))
#23.
bec="You cannot end a sentence with because because because is a conjunction"
print(bec.index("because"))
#24.
print(bec.rindex("because"))
#25.
delete="because because because"
new_bec=bec.replace(delete, "")
print(new_bec.strip())
#26.
print(bec.find("because"))
#27.
delete="because because because"
new_bec=bec.replace(delete, "")
print(new_bec.strip())
#28.
print(company.startswith("Coding"))
#29.
print(company.endswith("Coding"))
#30.
string="&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;"
new_string =string.strip()
print(new_string)
#31.
var1="30DaysOfPython"
var2="thirty_days_of_python"
print(var1.isidentifier())
print(var2.isidentifier())
#32.
bibliotecas=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
res="#" + " ".join(bibliotecas)
print(res)
#33.
print('I am enjoying this challenge.\nI just wonder what is next.')
#34.
print('Name\tAge\tCountry\tCity') 
print('Asabeneh\t250\tFinland\tHelsinki')
#35.
radius = 10
area = 3.14 * radius ** 2
formated_string = 'The area of a circle with a radius {} is {} meters square'.format(radius, area)
print(formated_string)
#36.
a=8
b=6
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

