def letter_checker():
    reverse_alphabet_list = ["Z", "Y", "X", "W", "V", "U", "T", "S", "R", "Q", "P", "O", "N", "M", "L", "K", "J", "I", "H", "G", "F", "E", "D", "C", "B", "A"]
    reverse_alphabet_string = "Z Y X W V U T S R Q P O N M L K J I H G F E D C B A"
    correct_letter_counter = 0
    entered_letters = ""

    for i in range(0, len(reverse_alphabet_list)):
        enter_letter = input("Enter a letter:")
        enter_letter = enter_letter.upper()

        if enter_letter == reverse_alphabet_list[i]:
            entered_letters = entered_letters + str(enter_letter) + " "
            correct_letter_counter += 1
            if enter_letter == "A" or enter_letter == "a":
                 return ("Correct letter count: "+ str(correct_letter_counter) + "\n" + "Correct entries: " + str(entered_letters) + "\n" + "Reverse Alphabet: " + reverse_alphabet_string + "\n" + "Congratulations! You reversed the Alphabet!")
        elif correct_letter_counter == 0:
            return ("Correct letter count: 0" + "\n" + "Reverse Alphabet: " + reverse_alphabet_string)
        else:
            if entered_letters != []:
                return ("Correct letter count: "+ str(correct_letter_counter) + "\n" + "Correct entries: " + str(entered_letters) + "\n" + "Reverse Alphabet: " + reverse_alphabet_string)
            exit()

print(letter_checker())
