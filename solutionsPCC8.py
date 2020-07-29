# PYTHON CRASH COURSE - Eric Matthes
# --Chapter 8: FUNCTIONS--
# 8.1 - Message:
def display_message():
    print("Today i am learning how to define a function")


display_message()


# 8.2 - Favorite Book:
def favorite_book(title):
    print(f"One of my favorite books is {title}")


favorite_book("Idoru")


# 8.3 - T-Shirt:
def make_shirt(size, text):
    print(f"You asked for a {size} sized shirt with the following message: {text}")


make_shirt("large", "Nerds will inherit the earth")
make_shirt(size="small", text="I have a white shirt")


# 8.4 - Large Shirts:
def make_shirt(size="large", text="I love Python"):
    print(f"You asked for a {size} sized shirt with the following message: {text}")


make_shirt()
make_shirt("medium")
make_shirt("small", "Get your hopes up, King!")


# 8.5 - Cities:
def describe_city(city, country="Colombia"):
    print(f"The city of {city} is located in {country}")


describe_city("Bogota")
describe_city("Leticia")
describe_city("Manila")


# 8.6 - City Names:
def city_country(city, country):
    print(f"{city}, {country}")


city_country("Johanesburg", "South Africa")
city_country("Rome", "Italy")
city_country("Lewiston", "U.S.A.")


# 8.7 - Album:
def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    print(album)


make_album("Metallica", "Hardwired")
make_album("Paramore", "Brand New Eyes")
make_album("Avantasia", "Ghostlights", "8")


# 8.8 - User Albums:
def make_album(artist, title, songs=0):
    album = {'Artist': artist.title(), 'Title': title.title()}
    if songs:
        album['songs'] = songs
    return album


print("If you wish to quit, press 'q' at anytime ")
while True:
    title = input("What album you want to add?")
    if title == 'q':
        break

    artist = input("Who is the artist behind the album?\n")
    if artist == 'q':
        break

    exposition = make_album(artist, title)
    print(exposition)


# 8.9 - Messages:
def show_messages(shortMessages):
    print("You received these messages:\n")
    for message in shortMessages:
        print(message)


message = ["I will be late tonight. Leave some dinner",
           "How about going to the Sea World this weekend?",
           "Going to the happy hour. See u later"]
show_messages(message)


# 8.10 - Sending messages:
def show_messages(shortMessages):
    print("You wish to send these messages:\n")
    for message in shortMessages:
        print(message)


def send_messages(message, sent_message):
    while message:
        sent = message.pop()
        print(" ")
        print(f"Sending message: {sent}")
        sent_message.append(sent)


message = ['I will be late tonight. Leave some dinner',
           "How about going to the Sea World this weekend?",
           "Going to the happy hour. See u later"]
sent_message = []
show_messages(message)
send_messages(message, sent_message)
print(message)
print(sent_message)


# 8.11 - Archived Messages:
def show_messages(shortMessages):
    print("You wish to send these messages:\n")
    for message in shortMessages:
        print(message)


def send_messages(message, sent_message):
    while message:
        sent = message.pop()
        print(f"\nSending message: {sent}")
        sent_message.append(sent)


message = ['I will be late tonight. Leave some dinner',
           "How about going to the Sea World this weekend?",
           "Going to the happy hour. See u later"]
sent_message = []
show_messages(message)
send_messages(message[:], sent_message)
print("\n", message)
print(sent_message)


# 8.12 - Sandwiches:
def sandwiches(*items):
    print("You ordered a sandwich with the following ingredients; ")
    for ingredients in items:
        print(f"- {ingredients}")


sandwiches("black bread", "ham", "cheese", "hamburger", "mayonnaise")
sandwiches("syrian bread", "meat", "pastrami", "bacon", "pickles", "mayonnaise")
sandwiches("bread", "lettuce")


# 8.13 - User profile:
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
chroma_profile = build_profile('Chromatic', 'Zero',
                               likes='sunsets',
                               dislikes='noise',
                               skincolor='iridescent')
print(chroma_profile)


# 8.14 - Cars:
def carInfo(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info


car_profile = carInfo('lamborghini', 'aventador',
                      horsepower='740hp',
                      debutYear='2011')
print(car_profile)
