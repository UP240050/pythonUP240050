#1.
Family_members=['Jimena', 'Fátima', 'Kiyomi', 'Alexa', 'Ikal', 'Andrés', 'Lourdes', 'Samuel']
family=list(Family_members)
Family=family[6:]
siblings=family[:6]
print(Family)
print(siblings)
#2.
frutas=['sandía', 'kiwi', 'piña', 'uva', 'limón']
vegetales=['brocoli', 'coliflor', 'espinaca', 'chayote', 'zanahoria']
animal_products=['leche', 'mariscos', 'queso', 'miel', 'carne']
food_stuff_tp=frutas+vegetales+animal_products
print(food_stuff_tp)
#3.
food_stuff_list=list(food_stuff_tp)
#4.
middle=food_stuff_list.pop(7)
print(middle)
#5.
print(food_stuff_tp[:3]+food_stuff_tp[-3:])
#6.
del food_stuff_tp
#7.
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
#7.1
print("Estonia" in nordic_countries)
#7.2
print("Iceland" in nordic_countries)