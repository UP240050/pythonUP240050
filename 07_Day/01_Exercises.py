it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

#1.
print(len(it_companies))
#2.
it_companies.add("Twitter")
print(it_companies)
#3.
it_companies.update(["WhatsApp", "Mason"],)
print(it_companies)
#4.
it_companies.remove("Facebook")
print(it_companies)
#5.
#Si se usa "remove" y un item no se encuentra en el set va a marcar el error.