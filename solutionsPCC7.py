# 7.1 - Rental Car:
car = input("What kind of car would you like to rent? ")
print(f"Let me see if I can find you a {car}")

# 7.2 - Restaurant Seating:
dinnerGroup = int(input("How many people are you bringing in today? "))
if dinnerGroup > 8:
    print("Your group has to wait for a table to be vacant")
else:
    print("Your table is ready. Please, follow me")

# 7.3 - Multiples of ten
nbr = int(input("Enter a number: "))
if nbr % 10 != 0:
    print("This is not a multiple of ten")
else:
    print("This is a multiple of ten")

# 7.4 - Pizza Toppings:
active = True
while active:
    toppings = input("Enter a pizza topping: ")

    if toppings == "quit":
        active = False
    else:
        print(f"adding {toppings}")

# 7.5 - Movie Tickets:
askAgain = True
while askAgain:
    ask = int(input("What is your age? "))
    if ask < 3:
        print("Ticket Price: Free")
    elif 3 < ask < 12:
        print("Ticket Price: 10$")
    else:
        print("Ticket Price: 15$")

# 7.6 - Three Exits:
toppings = input("Enter a pizza topping: ")  # Version that shuts down the execution by a condition in while
while toppings != "jalapeno":
    toppings = input("Enter a pizza topping: ")

active = True  # Version that uses a "active" variable to control how long the program runs (original version of the
# program I wrote [go see example 7.4 - Pizza Toppings for reference])
while active:
    toppings = input("Enter a pizza topping: ")

    if toppings == "quit":
        active = False
    else:
        print(f"adding {toppings}")

print("Please enter a topping. Enter 'quit' when you done")  # In this version we interrupt the execution by using the
# 'break' statement. Personally... I really prefer the use of an active variable. I think it just stuck with me.
while True:
    toppings = input(" ")
    if toppings == "quit":
        break
    else:
        print(f"adding {toppings}")

# 7.7 - Infinite Loop:
while True:
    print("Are we falling?")

# 7.8 - Deli:
sandwich_orders = ["Rib", "Full House", "Pastrami", "Tuna", "Western Flavour"]
finished_sandwiches = []
while sandwich_orders:
    finished_order = sandwich_orders.pop()
    print("I'm working on your " + finished_order + " sandwich.")
    finished_sandwiches.append(finished_order)
print(" ")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")

# 7.9 - No Pastrami:
sandwich_orders = ["Pastrami", "Rib", "Full House", "Pastrami", "Tuna", "Western Flavour", "Pastrami"]
finished_sandwiches = []
print("The deli ran out of Pastrami")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
while sandwich_orders:
    finished_order = sandwich_orders.pop()
    print("I'm working on your " + finished_order + " sandwich.")
    finished_sandwiches.append(finished_order)
print(" ")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")

# 7.10 - Dream Vacation:
responses = {}
active = True
while active:
    name = input("What is your name?")
    destination = input("Which place would you like to visit in your vacations?")
    responses[name] = destination
    loop = input("Will somebody else take the poll? (y/n)")
    if loop == "n":
        active = False
print("###RESULTS###")
for name, destination in responses.items():
    print(f"{name} would like to travel to {destination}")
