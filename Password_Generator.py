import random


def password():
    lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    special_characters = ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "[", "]", "{", "}", "|", ":", ";", "'", "<", ",", ">", ".", "?", "/"]

    choose_from = [0, 1, 2, 3]
    choose_from2 = [0, 1, 2, 3]

    first_four_letters = ""
    last_four_letters = ""

    while len(first_four_letters) < 4:
        new_character = random.choice(choose_from)

        if random.choice(choose_from) == 0 and random.choice(choose_from) != "":
            random.selection = random.choice(lowercase)
            first_four_letters = first_four_letters + random.selection
            choose_from[0] == ""

        if random.choice(choose_from) == 1 and random.choice(choose_from) != "":
            random.selection = random.choice(uppercase)
            first_four_letters = first_four_letters + random.selection
            choose_from[1] == ""

        if random.choice(choose_from) == 2 and random.choice(choose_from) != "":
            random.selection = random.choice(numbers)
            first_four_letters = first_four_letters + random.selection
            choose_from[2] == ""

        if random.choice(choose_from) == 3 and random.choice(choose_from) != "":
            random.selection = random.choice(special_characters)
            first_four_letters = first_four_letters + random.selection
            choose_from[3] == ""


    while len(last_four_letters) < 4:
        new_character = random.choice(choose_from2)

        if random.choice(choose_from2) == 0 and random.choice(choose_from) != "":
            random.selection = random.choice(lowercase)
            last_four_letters = last_four_letters + random.selection
            choose_from2[0] == ""

        if random.choice(choose_from2) == 1 and random.choice(choose_from) != "":
            random.selection = random.choice(uppercase)
            last_four_letters = last_four_letters + random.selection
            choose_from2[1] == ""

        if random.choice(choose_from2) == 2 and random.choice(choose_from) != "":
            random.selection = random.choice(numbers)
            last_four_letters = last_four_letters + random.selection
            choose_from2[2] == ""

        if random.choice(choose_from2) == 3 and random.choice(choose_from) != "":
            random.selection = random.choice(special_characters)
            last_four_letters = last_four_letters + random.selection
            choose_from2[3] == ""

    generated_password = first_four_letters + last_four_letters
    return generated_password

print("The password generated is: " + password())