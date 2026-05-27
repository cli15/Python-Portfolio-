#Christina
#Madlibs story
#Allow user for inputs and randomly sort them into a story

#Functions
import random

def madlibs():
    print("Let's play madlibs!")
    day = input("Pick a day of the week: ")
    if day == "random":
        list1 = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        day = random.choice(list1)
    place = input("Pick a place: ")
    if place == "random":
        list2 = ["Target", "Walmart", "CVS","Walgreens"]
        place = random.choice(list2)
    adjective = input("Pick an adjective: ")
    if adjective == "random":
        list3 = ["awful","happy","amazing","chill"]
        adjective = random.choice(list3)
    name = input("Pick a name: ")
    if name == "random":
        list4 = ["Chris","Bob","Ross","Bill"]
        name = random.choice(list4)
    food = input("Pick a food (plural): ")
    if food == "random":
        list5 = ["burgers","fries","sandwhiches","salads"]
        food = random.choice(list5)
    verb = input("Pick a ING verb: ")
    if verb == "random":
        list6 = ["running", "walking", "talking", "hopping"]
        verb = random.choice(list6)
    noun = input("Pick a noun: ")
    if noun == "random":
        list7 = ["toy","keychain","eraser","pen"]
        noun = random.choice(list7)
    print(f"""Today is \033[1m{day.upper()}\033[0m and I went to \033[1m{place.upper()}\033[0m.
    It was \033[1m{adjective.upper()}\033[0m. Me and \033[1m{name.upper()}\033[0m ate {food.upper()}\033[1m, while \033[1m{verb.upper()}\033[0m.
    Then, we went to a shop and I bought a \033[1m{noun.upper()}\033[0m.
    I was really happy because I've wanted one for a while.""")

#Main
madlibs()



