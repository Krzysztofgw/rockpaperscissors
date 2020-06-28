import random

option_list = ["rock", "fire", "scissors", "snake", "human", "tree", "wolf", "sponge", "paper", "air",
               "water", "dragon", "devil", "lightning", "gun"]
option = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

user_input = ""
dict_rating = {}


def rating():
    global dict_rating, file
    file = open(file_name, 'r+')
    for i in file:
        list_rating = i.split(" ")
        dict_rating[list_rating[0]] = int(list_rating[1].rstrip("\n"))
    if name in dict_rating.keys():
        pass
    else:
        dict_rating[name] = 0
    file.close()


def write_points():
    global file
    file = open(file_name, 'w+')
    for i in dict_rating:
        print("{} {}".format(i, dict_rating[i]), file=file)


def add_points(points):
    global dict_rating
    dict_rating[name] = dict_rating[name] + points


def options():
    global option_list, option
    user_options = input()
    if user_options != "":
        option_holder = user_options.split(",")
        for i in option_holder:
            if option_list.index(i) < 9:
                option[i] = option_list[option_list.index(i):option_list.index(i) + 8]
            else:
                option[i] = option_list[option_list.index(i):option_list.index(i) - 8:-1]
        option_list = option_holder
    else:
        option_list = ["rock", "scissors", "paper"]


print("Input your name:", end=" ")
name = input()
print("Hello, {}".format(name))
file_name = 'rating.txt'
rating()
options()
print("Okay, let's start")
while True:
    user_input = input()
    if user_input == "!exit":
        print("Bye!")
        break
    if user_input == "!rating":
        print("Your rating: {}".format(dict_rating[name]))
        continue
    computer = random.choice(option_list)
    if user_input in option:
        if user_input == computer:
            print("There is a draw ({})".format(computer))
            add_points(50)
        else:
            if user_input in option[computer] and option_list.index(user_input) > len(option_list) // 2:
                print("Sorry, but computer chose {}".format(computer))
            else:
                print("Well done. Computer chose {} and failed".format(computer))
                add_points(100)
    else:
        print("Invalid input")
write_points()
