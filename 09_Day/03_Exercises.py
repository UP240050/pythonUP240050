#1.
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

#1.2
if 'skills' in person:
    skills = person['skills']
    central_skill = skills[len(skills) // 2]  
    print("Habilidad central:", central_skill)

#1.3
if 'Python' in person['skills']:
        print('La persona tiene la habilidad de Python')
else:
        print('La persona no tiene la habilidad de Python')

#1.4
if 'JavaScript' in 'skills' and 'React' in 'skills' and len('skills') == 2:
        print("He is a front end developer")
elif 'Node' in 'skills' and 'Python' in 'skills' and 'MongoDB' in 'skills':
        print("He is a backend developer")
elif 'React' in 'skills' and 'Node' in 'skills' and 'MongoDB' in 'skills':
        print("He is a fullstack developer")
else:
        print("Unknown title")

#1.5
if person['is_marred'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")