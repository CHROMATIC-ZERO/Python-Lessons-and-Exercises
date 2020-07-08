# PYTHON CRASH COURSE - Eric Matthes
# --CHAPTER 3: Introducing Lists --
# 3.1 - Names:
names = ['Tim', 'Mina', 'Ken']
print(names[0])
print(names[1])
print(names[2])
# 3.2 - Greetings:
names = ['Tim', 'Mina', 'Ken']
print("Hey,", names[0], ". Welcome!")
print("Hey,", names[1], ". Welcome!")
print("Hey,", names[2], ". Welcome!")
# 3.3 - Your own list:
cars = ['Audi', 'BMW', 'Lancia', 'Aston Martin']
print("I would like to own a", cars[0])
print("I would like to own a", cars[1])
print("I would like to own a", cars[2])
print("I would like to own a", cars[3])
# 3.4 - Guest List:
guests = ["Elvis", "Haruki Murakami", "Elon Musk"]
print("We are pleased to receive in tonight dinner's:", guests[0])
print("We are pleased to receive in tonight dinner's:", guests[1])
print("We are pleased to receive in tonight dinner's:", guests[2])
# 3.5 - Changing Guest List:
guests = ["Elvis", "Haruki Murakami", "Elon Musk"]
print("We are pleased to receive in tonight dinner's:", guests[0])
print("We are pleased to receive in tonight dinner's:", guests[1])
print("We are pleased to receive in tonight dinner's:", guests[2])
print("####")
print("Unfortunately; mr. Elvis won't make to the dinner")
guests[0] = "Nikolai II"
print("####")
print("We are pleased to receive in tonight dinner's:", guests[0])
print("We are pleased to receive in tonight dinner's:", guests[1])
print("We are pleased to receive in tonight dinner's:", guests[2])
# 3.6 - More Guests:
guests = ["Elvis", "Haruki Murakami", "Elon Musk"]
print("We are pleased to receive in tonight dinner's:", guests[0])
print("We are pleased to receive in tonight dinner's:", guests[1])
print("We are pleased to receive in tonight dinner's:", guests[2])
print("####")
print("Unfortunately; mr. Elvis won't make to the dinner")
guests[0] = "Nikolai II"
print("####")
print("We are pleased to receive in tonight dinner's:", guests[0])
print("We are pleased to receive in tonight dinner's:", guests[1])
print("We are pleased to receive in tonight dinner's:", guests[2])
print("####")
print("Fortune has smiled upon us, as I have found a bigger dinner table")
print("####")
guests.insert(0, "Amelia Earhart")
guests.insert(3, "Amy Lee")
guests.append("Ada Lovelace")
print("We are pleased to receive in tonight dinner's:", guests[0])
print("We are pleased to receive in tonight dinner's:", guests[1])
print("We are pleased to receive in tonight dinner's:", guests[2])
print("We are pleased to receive in tonight dinner's:", guests[3])
print("We are pleased to receive in tonight dinner's:", guests[4])
print("We are pleased to receive in tonight dinner's:", guests[5])
# 3.7 - Shrinking Guest List:
guests = ["Elvis", "Haruki Murakami", "Elon Musk"]
print("We are pleased to receive in tonight dinner's:", guests[0])
print("We are pleased to receive in tonight dinner's:", guests[1])
print("We are pleased to receive in tonight dinner's:", guests[2])
print("####")
print("Unfortunately; mr. Elvis won't make to the dinner")
guests[0] = "Nikolai II"
print("####")
print("We are pleased to receive in tonight dinner's:", guests[0])
print("We are pleased to receive in tonight dinner's:", guests[1])
print("We are pleased to receive in tonight dinner's:", guests[2])
print("####")
print("Fortune has smiled upon us, as I have found a bigger dinner table")
print("####")
guests.insert(0, "Amelia Earhart")
guests.insert(3, "Amy Lee")
guests.append("Ada Lovelace")
print("We are pleased to receive in tonight dinner's:", guests[0])
print("We are pleased to receive in tonight dinner's:", guests[1])
print("We are pleased to receive in tonight dinner's:", guests[2])
print("We are pleased to receive in tonight dinner's:", guests[3])
print("We are pleased to receive in tonight dinner's:", guests[4])
print("We are pleased to receive in tonight dinner's:", guests[5])
print("####")
print("Misfortune hits our event. As the table won't arrive on time")
print("####")
elimination1 = guests.pop()
print("I'm deeply sorry", elimination1, ". I have to uninvite you")
elimination2 = guests.pop()
print("I'm deeply sorry", elimination2, ". I have to uninvite you")
elimination3 = guests.pop()
print("I'm deeply sorry", elimination3, ". I have to uninvite you")
elimination4 = guests.pop()
print("I'm deeply sorry", elimination4, ". I have to uninvite you")
print("On the other hand. I'm so happy you still will be with us Mr(s).", guests[0])
print("On the other hand. I'm so happy you still will be with us Mr(s).", guests[1])
del guests[0]
print(guests)
del guests[0]
print(guests)
# 3.8 - Seeing the World:
places = ["Palermo", "Monaco", "Seattle", "Reykjavik", "Kobe"]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
# 3.9 - Dinner Guests:
guests = ["Elvis", "Haruki Murakami", "Elon Musk"]
print("We are pleased to receive in tonight dinner's:", guests[0])
print("We are pleased to receive in tonight dinner's:", guests[1])
print("We are pleased to receive in tonight dinner's:", guests[2])
print("####")
print("Unfortunately; mr. Elvis won't make to the dinner")
guests[0] = "Nikolai II"
print("####")
print("We are pleased to receive in tonight dinner's:", guests[0])
print("We are pleased to receive in tonight dinner's:", guests[1])
print("We are pleased to receive in tonight dinner's:", guests[2])
print("####")
print("Fortune has smiled upon us, as I have found a bigger dinner table")
print("####")
guests.insert(0, "Amelia Earhart")
guests.insert(3, "Amy Lee")
guests.append("Ada Lovelace")
print("We are pleased to receive in tonight dinner's:", guests[0])
print("We are pleased to receive in tonight dinner's:", guests[1])
print("We are pleased to receive in tonight dinner's:", guests[2])
print("We are pleased to receive in tonight dinner's:", guests[3])
print("We are pleased to receive in tonight dinner's:", guests[4])
print("We are pleased to receive in tonight dinner's:", guests[5])
print("To this event I invited", len(guests), "people")
# 3.10 Every function:
languages = ["english", "spanish", "russian", "yiddish", "norwegian"]
reservation = []
print(languages[3])
languages[0] = "esperanto"
languages.insert(3, "french")
retirement = languages.pop()
reservation.append(retirement)
del languages[2]
print(sorted(languages))
print(sorted(languages, reverse=True))
languages.reverse()
print(languages)
languages.sort()
print(languages)
languages.sort(reverse=True)
print(languages)
print(retirement)
print("The len of the final list after all alterations is of", len(languages), "items")
