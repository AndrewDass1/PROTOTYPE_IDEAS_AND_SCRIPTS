ask_for_voltage = float(input("Enter voltage : "))

ask_for_current = float(input("Enter current : "))

calculate_resistance = ask_for_voltage / ask_for_current

print("The resistance is :", calculate_resistance)

if calculate_resistance < 1:
    print("The resistance is low")
elif calculate_resistance > 1 and calculate_resistance < 100000:
    print("The resistance is medium")
elif calculate_resistance > 100000:
    print("The resistance is high")
else:
    print("Invalid operation")
