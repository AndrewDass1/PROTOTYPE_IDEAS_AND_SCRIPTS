enter_a_number = int(input("Enter a number:"))
absolute_value_number = abs(enter_a_number)

starting_value = 2
stores_composite_values = []


if absolute_value_number == 0:
    print("0 is not a unique, prime or composite number")
elif absolute_value_number == 1:
    print("1 is a unique number")
elif absolute_value_number > 1:
    entered_number = absolute_value_number
    for i in range(2, entered_number):
        division = entered_number / starting_value
        rounded_division = entered_number // starting_value

        if entered_number / i == entered_number // i:
            pair_of_multiples = (rounded_division, starting_value)
            stores_composite_values.append(pair_of_multiples)
        starting_value += 1

    if stores_composite_values == []:
        print(str(absolute_value_number) + " is a prime number with multiples of :" + "\n" + "(" + str(absolute_value_number)+", 1)" + "\n" + "(1, " + str(absolute_value_number) + ")" )
    else:
        print(str(absolute_value_number) + " is a composite number with the following multiples:")
        print( "("+str(absolute_value_number)+",", "1)")
        for i in range(0, len(stores_composite_values)):
            print(stores_composite_values[i])
        print("(1,", str(absolute_value_number)+")")

else:
    print("Invalid number.")
