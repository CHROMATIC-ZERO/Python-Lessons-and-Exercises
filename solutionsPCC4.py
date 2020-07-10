# PYTHON CRASH COURSE - Eric Matthes
# --CHAPTER 4: Working with Lists --
# 4.1 - Pizzas:
pizzas = ["Portuguese", "Tuna", "Sweet"]
for flavors in pizzas:
    print(flavors)
    print(" ")
for flavors in pizzas:
    print("I like", flavors, "pizza")
print("I reeeally love pizza. I would kill for some as of right now")
# 4.2 - Animals:
animals = ["yak", "bison", "bull"]
for types in animals:
    print(types)
    print(" ")
for types in animals:
    print("A", types, "has some big horns")
print("All of these animals are part of the bovidae family")
# 4.3 - Counting to Twenty:
for number in range(1, 21):
    print(number)
# 4.4 - One Million:
millionList = list(range(1, 1000001))
for nbr in millionList:
    print(nbr)
# 4.5 - Summing a Million:
millionList = list(range(1, 1000001))
print("This list starts at", min(millionList))
print("And it ends in", max(millionList))
print("The sum of all its numbers equals", sum(millionList))
# 4.6 - Odd Numbers:
odds = list(range(1, 21, 2))
for nbr in odds:
    print(nbr)
# 4.7 - Threes:
multiples = []
for value in range(3, 31):
    multiple = value * 3
    multiples.append(multiple)
print(multiples)
# 4.8 - Cubes:
cubes = []
for value in range(1, 11):
    cube = value ** 3
    cubes.append(cube)
print(cubes)
# 4.9 - Cube Comprehension:
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)
# 4.10 - Slices:
pizzas = ["Portuguese", "Tuna", "Sweet", "Bacon", "Shrooms"]
for flavors in pizzas:
    print(flavors)
    print(" ")
for flavors in pizzas:
    print("I like", flavors, "pizza")
print("I reeeally love pizza. I would kill for some as of right now")
print("The first three items in the list are:", pizzas[0:3])
print("The three middle items in the list are:", pizzas[1:4])
print("The last three items in the list are:", pizzas[2:5])
# 4.11 - My Pizzas, Your Pizzas:
pizzas = ["Portuguese", "Tuna", "Sweet"]
friends_pizzas = pizzas[:]
for flavors in pizzas:
    print(flavors)
    print(" ")
for flavors in pizzas:
    print("I like", flavors, "pizza")
print("I reeeally love pizza. I would kill for some as of right now")
pizzas.append("Shrimp")
friends_pizzas.append("Veggie")
for flavors in pizzas:
    print("My favorite pizzas are:", flavors)
for flavours in friends_pizzas:
    print("My friend's favorite pizzas are:", flavours)
# 4.12 - More Loops:
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favourite foods are:")
for options in my_foods:
    print(options)
print("\nMy friend's favourite foods are:")
for option in friend_foods:
    print(option)
# 4.13 - Buffet:
menu_items = ("Lobster", "Meat Pie", "Casserole", "Brazilian Beans", "Bratwurst")
print("These are the items in our current menu:")
for foods in menu_items:
    print(foods)
menu_items = ("Lobster", "Humus", "Casserole", "Reuben", "Bratwurst")
print("\nLong time no see! This is our new menu:")
for foods in menu_items:
    print(foods)
