import time

#time.sleep()

def letter_checker():
    reverse_alphabet_list = ["Z", "Y", "X", "W", "V", "U", "T", "S", "R", "Q", "P", "O", "N", "M", "L", "K", "J", "I", "H", "G", "F", "E", "D", "C", "B", "A"]
    correct_letter_counter = 0
    entered_letters = []

    for i in range(0, len(reverse_alphabet_list)):
        enter_letter = input("")
        enter_letter = enter_letter.upper()

        if enter_letter == reverse_alphabet_list[i]:
            entered_letters.append(enter_letter)
            correct_letter_counter += 1
        else:
            if entered_letters != []:
                print("Correct Entries:", end="")
                print(entered_letters)
                print("Correct letter count: "+ str(correct_letter_counter) )
            exit()
