#1.
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filt_nums = [num for num in numbers if num <=0]
print(filt_nums)

#2.
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [item for sublist in list_of_lists for item in sublist [0]]
print(flattened_list)

#3.
nums= [(i,1, i**2,i**3,i**4,i**5) for i in range(0,11)]
print(nums)

#4.
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatten_countries = [item for sublist in countries for item in sublist [0]]
cap_countries = [i.upper() for i in flatten_countries]
print (cap_countries)

#5.
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_dict = [{"country": item[0][0].upper(), "city": item[0][1].upper()} for item in countries]
print(countries_dict)

#6.
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
lst_names=[' '.join(name[0]) for name in names]
print(lst_names)

#7.
pend = lambda x1,x2,y1,y2 : (y2-y1) / (x2-x1)
intersection_y=lambda m,x1,y1 : y1-m*x1
x1 = 3
x2 = 5
y1 = 2
y2 = 1
m = pend (x1,x2,y1,y2)
print ("La pendiente es: ", m)
a = intersection_y(m,x1,y1)
print ("La intersección en y es: ",a)