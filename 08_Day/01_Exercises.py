#1.
dog = {}
#2.
dog = {'name':'Toby', 'color':'brown', 'breed':'pastor alemán', 'legs':'4', 'age':'5'}
#3.
student_dictionary = {'First name':'Mauricio', 'Last name':'Purón', 'Gender':'masculino', 'Age':'22', 'Martial status':'soltero', 'Skills':['futbol', 'guitarra', 'idiomas'], 'Country':'España', 'City':'Valencia', 'Address':'Valencia #506'}
#4.
print(len(student_dictionary))
#5.
values = student_dictionary.values()
print(values)
print(type(values))
#6.
student_dictionary['age'] = '30'
print(student_dictionary)
#7.
keys = student_dictionary.keys()
print(keys)
#8.
values = student_dictionary.values()
print(values)
#9.
student_tuples = list(student_dictionary.items())
print(student_tuples)
#10.
student_dictionary.pop('Skills')
#11.
del student_dictionary
