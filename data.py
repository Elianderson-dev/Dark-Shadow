import random
#This function is for select letters to user password
def select_the_letters (letters):
    number_of_values = range(0, 5)

    letters = ["a","b","c","d","e","f","g","h","i"
    "j", "k", "l", "m", "n", "o", "p", "q", "r",
     "s", "t", "u", "v", "w", "x", "y", "z"]

    for values in number_of_values:
        take_the_letters = random.choice(letters)

def select_the_numbers (numbers):
    number_of_values = range(0, 5)

    for values in number_of_values:
        take_the_numbers = random.randint(0, 10)

#Save password data


    