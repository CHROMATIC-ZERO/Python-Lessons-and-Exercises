# PYTHON CRASH COURSE - Eric Matthes
# --Chapter 6: Dictionaries--
# 6.1 - Person:
personInfo = {'first_name': 'Ken', 'last_name': 'Hiroshi', 'age': '21', 'city': 'Osaka'}
print("Our client is a mr.", personInfo['first_name'])
print("Last name is:", personInfo['last_name'])
print("He is", personInfo['age'], "years old")
print("And lives in", personInfo['city'])

# 6.2 - Favorite Numbers:
FavNbr = {'Ken': '5', 'William': '13', 'Jenny': '100', 'Mina': '38', 'Alanis': '9'}
print("Ken favourite number is", FavNbr['Ken'])
print("William favourite number is", FavNbr['William'])
print("Jenny favourite number is", FavNbr['Jenny'])
print("Mina favourite number is", FavNbr['Mina'])
print("Alanis favourite number is", FavNbr['Alanis'])

# 6.3 - Glossary
words = {'Print': 'Displays a message',
         'Variable': 'Container able to store data',
         'Object': 'Simple collection of data and methods that act on the data',
         'Def': 'Defines a variable by setting a number of steps to its execution',
         'Dictionary': 'Method of connecting pieces of related information'}
print("Print:", words['Print'], "\n")
print("Variable:", words['Variable'], "\n")
print("Object:", words['Object'], "\n")
print("Def:", words['Def'], "\n")
print("Dictionary:", words['Dictionary'], "\n")

# 6.4 - Glossary 2:
words = {'Print': 'Displays a message',
         'Variable': 'Container able to store data',
         'Object': 'Simple collection of data and methods that act on the data',
         'Def': 'Defines a variable by setting a number of steps to its execution',
         'Dictionary': 'Method of connecting pieces of related information',
         'For': 'Loop that iterates over a sequence',
         'While': 'Loop that operates while a given condition meets its requirements',
         'Boolean': 'Condition able to evaluate an expression to True or False',
         'Key': 'Denomination used to access a value',
         'Value': 'Association to the key that assumes a representative value to it'}
for word, definition in words.items():
    print(f"\n{word}: {definition}")

# 6.5 - Rivers:
rivers = {'Amazonas': 'Brazil', 'Mississippi': 'U.S.A.', 'Yangtze': 'China'}
for river, country in rivers.items():
    print(f"\nThe {river} flows through the lands of {country}")
print()
for river in rivers.keys():
    print(river)
print()
for country in rivers.values():
    print(country)

# 6.6 - Polling:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

pollParticipants = ('alan', 'lewis', 'yuki', 'jen', 'peyton', 'sarah')

for people in pollParticipants:
    if people in favorite_languages:
        print(f'\nHey, {people.title()}! Glad you took our poll')
    else:
        print(f'\nHey, {people.title()}! Go take our poll, it is in our homepage!')

# 6.7 - People:
people = []
personInfo = {'first_name': 'Ken', 'last_name': 'Hiroshi', 'age': '21', 'city': 'Osaka'}
people.append(personInfo)
personInfo2 = {'first_name': 'Avi', 'last_name': 'Isaacson', 'age': '48', 'city': 'Tel Aviv'}
people.append(personInfo2)
personInfo3 = {'first_name': 'Mina', 'last_name': 'Harker', 'age': '30', 'city': 'Liverpool'}
people.append(personInfo3)
for individual in people:
    print("Our client is a mr(s).", individual['first_name'])
    print("Last name is:", individual['last_name'])
    print("(S)He is", individual['age'], "years old")
    print("And lives in", individual['city'], "\n")

# 6.8 - Pets:
pets = []
petInfo = {'name': 'Mia', 'species': 'Cat', 'age': '3', 'owner': 'Ken'}
pets.append(petInfo)
petInfo2 = {'name': 'Bobby', 'species': 'Parrot', 'age': '13', 'owner': 'Edward'}
pets.append(petInfo2)
petInfo3 = {'name': 'Spike', 'species': 'Dog', 'age': '8', 'owner': 'Nigel'}
pets.append(petInfo3)
petInfo4 = {'name': 'Noodle-Noodle', 'species': 'Snake', 'age': '1', 'owner': 'Kim'}
pets.append(petInfo4)
petInfo5 = {'name': 'Max', 'species': 'Bearded Dragon', 'age': '3', 'owner': 'James'}
pets.append(petInfo5)
petInfo6 = {'name': 'Sadaharu', 'species': 'Dog', 'age': '?', 'owner': 'Kagura'}
pets.append(petInfo6)
for animals in pets:
    print("This animal is called", animals['name'])
    print("(S)He is a", animals['species'])
    if animals['age'] == '?':
        print("Well, we do not really know his(her) age...")
    else:
        print("(S)He is", animals['age'], "years old")
    print("And his(her) owner is a Mr(s).", animals['owner'], "\n")

# 6.9 - Favorite places:
favPlaces = {'Alan': ['Berlin', 'Zurich', 'Nice'],
             'João': ['Chapada dos Veadeiros', 'Bonito', 'Gramado'],
             'Reiko': ['Bangkok', 'Mie', 'Shanghai']}
for names, places in favPlaces.items():
    print(f"\n{names} favourite places are: ")
    for location in places:
        print(f"\t{location}")

# 6.10 - Favorite Numbers:
FavNbr = {'Ken': ['5', '10', '15'],
          'William': ['13', '4', '17'],
          'Jenny': ['100', '300', '911'],
          'Mina': ['38', '56', '62'],
          'Alanis': ['3', '5', '8']}
for person, numbers in FavNbr.items():
    print(f"{person} favorite numbers are:\n")
    for unities in numbers:
        print(f"\t{unities}")

# 6.11 - Cities:
cities = {'Denver': {
              'country': 'USA',
              'population': '619968',
              'fact': 'Denver has been named the “Baby Boomer Capital of America”'},
          'Reykjavik': {
              'country': 'Iceland',
              'population': '122853',
              'fact': 'Reykjavik is the Northernmost capital of the world'},
          'Bangkok': {
              'country': 'Thailand',
              'population': '8281000',
              'fact': 'Bangkok has the longest city name in the World'}}
for towns, info in cities.items():
    country = info['country']
    population = info['population']
    fun_facts = info['fact']

    print("\n" + towns.title() + " is in " + country + ".")
    print("  It has a population of about " + str(population) + ".")
    print(" fun fact:", fun_facts)

# 6.12 - Extensions:
users = {'user_0': {
 'username': 'efermi',
 'first': 'Enrico',
 'last': 'Fermi'},
 'user_1': {
 'username': 'mOOnMooN',
 'first': 'Ken',
 'last': 'Shiota'}}

for user, info in users.items():
    full_name = f"{info['first']} {info['last']}"
    nick = info['username']
    print(f"Welcome! {nick}")
    print(f"For security reasons, is your name", full_name, "?\n")


