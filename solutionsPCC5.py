# PYTHON CRASH COURSE - Eric Matthes
# --Chapter 5: If Statements--
# 5.1 - Conditional Tests:
car = "Land Rover"
print("Is car == 'Land Rover'? I predict True")
print(car == "Land Rover")
print("Is car == 'Ferrari'? Doubt. 'prolly' False")
print(car == "Ferrari")
favFood = "Pasta"
print("Is my favourite food == 'Pasta'? Yes. it is True")
print(favFood == "Pasta")
print("Is my favourite food == 'Fish'? Yuck. it is False")
print(favFood == "Fish")
favCloth = "Jacket"
print("My favourite piece of cloth == 'Jacket'? You can bet on it. True")
print(favCloth == "Jacket")
print("My favourite piece of cloth == 'Tank Top'? Wrong. False")
print(favCloth == "Tank Top")
animal = "Dog"
print("My favourite animal == 'Dog?' It is the best household animal. True")
print(animal == "Dog")
print("My favourite animal == 'Cat'? Yeah, I'm not a 40 year old weirdo. False")
print(animal == "Cat")
instrument = "Cello"
print("My favourite instrument == 'Cello'? Cult yet rad. True")
print(instrument == "Cello")
print("My favourite instrument == 'Guitar'? Talk about cliché. False")
print(instrument == "Guitar")

# 5.3 - Alien colors #1:
alien_color = "green"
if alien_color == "green":
    print("You just earned 5 points!")
alien_color = "red"
if alien_color == "green":
    print("You just earned 5 points!")

# 5.4 - Alien Colors #2:
alien_color = "green"
if alien_color == "green":
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")
alien_color = "red"
if alien_color == "green":
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

# 5.4 - Alien Colors #3:
alien_color = "green"
if alien_color == "green":
    print("You just earned 5 points!")
elif alien_color == "yellow":
    print("You just earned 10 points!")
elif alien_color == "red":
    print("You just earned 15 points!")
alien_color = "yellow"
if alien_color == "green":
    print("You just earned 5 points!")
elif alien_color == "yellow":
    print("You just earned 10 points!")
elif alien_color == "red":
    print("You just earned 15 points!")
alien_color = "red"
if alien_color == "green":
    print("You just earned 5 points!")
elif alien_color == "yellow":
    print("You just earned 10 points!")
elif alien_color == "red":
    print("You just earned 15 points!")

# 5.6 - Stages of life:
age = 23
if age < 2:
    print("This person is a baby")
elif 2 < age < 4:
    print("This person is a toddler")
elif 4 < age < 13:
    print("This person is a child")
elif 13 < age < 20:
    print("This person is a teenager")
elif 20 < age < 65:
    print("This person is an adult")
else:
    print("This person is a elder")

# 5.7 - Favorite Fruit:
favFruit = ["Banana", "Apple", "Pineapple"]
if "Dragonfruit" in favFruit:
    print("You really like Dragonfruits")
if "Banana" in favFruit:
    print("You really like Bananas")
if "Lime" in favFruit:
    print("You really like Limes")
if "Apple" in favFruit:
    print("You really like Apples")
if "Pineapple" in favFruit:
    print("You really like Pineapples")

# 5.8 - Hello Admin:
userNames = ["ElectricFranz90", "C_H_E_E_S_E__G_U_Y", "admin", "NightKnight89", "MOoNMooN"]

for users in userNames:
    if users == "admin":
        print("Hello admin! Here are the reports you asked for: ")
    else:
        print("Hello", users, ". Thanks for using our platform")

# 5.9 - No Users:
userNames = []

for users in userNames:
    if users == "admin":
        print("Hello admin! Here are the reports you asked for: ")
    else:
        print("Hello", users, ". Thanks for using our platform")
if len(userNames) == 0:
    print("We need to find some users!")

# 5.10 - Checking Usernames:
current_users = ['uMustBJoeKing', 'ChuqNoia', 'TeneT', 'erinBAKER', 'kimjongtwo']
new_users = ['7lynne7', 'chuqnoia', 'MarkTheDark', 'everglowing', 'tenet']

current_users_ = [user.lower() for user in current_users]

for newUser in new_users:
    if newUser.lower() in current_users_:
        print("Hey " + newUser + ", that name is already taken.")
    else:
        print("Great, " + newUser + " is still available. Let's head to the next steps")
        
# 5.11 - Ordinal Numbers:
ordinal = list(range(1, 10))
for number in ordinal:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number)+"th")
