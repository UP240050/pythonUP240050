#1.
empty_list=list()
print(empty_list)
#2.
spain_cities=['Barcelona', 'Madrid', 'Valencia', 'Sevilla', 'Zaragoza', 'Girona', 'Bilbao']
#3.
print(len(spain_cities))
#4.
first_city=spain_cities[0]
print(first_city)
middle_city=spain_cities[3]
print(middle_city)
last_city=spain_cities[6]
print(last_city)
#5.
mixed_data_types=['Yaretzi', '19', '1.63', 'single', 'Chichen Itza #102 Lomas de Jesús María']
#6.
it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IMB', 'Oracle', 'Amazon']
#7.
print(it_companies)
#8.
print(len(it_companies))
#9.
first_company=it_companies[0]
print(first_company)
middle_company=it_companies[3]
print(middle_company)
last_company=it_companies[6]
print(last_company)
#10.
it_companies[2]="WhatsApp"
print(it_companies)
#11.
it_companies.append("Oracle")
#12.
it_companies.insert(3, "Mason")
#13.
it_companies[5].upper()
#14.
print('#; '.join(it_companies))
#15.
exist='Apple'in it_companies
print(exist)
#16.
it_companies.sort()
print(it_companies)
#17.
it_companies.reverse()
print(it_companies)
#18.
print(it_companies[3:])
#19.
print(it_companies[:6])
#20.
print(it_companies[:4]+it_companies[5:])
#21.
it_companies.pop(0)
print(it_companies)
#22.
it_companies.pop(3)
print(it_companies)
it_companies.pop(3)
print(it_companies)
#23.
it_companies.pop()
print(it_companies)
#24.
del it_companies[:]
print(it_companies)
#25.
del it_companies
#26.
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)
#27.
full_stack=front_end
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)