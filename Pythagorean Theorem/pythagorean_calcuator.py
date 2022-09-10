enter_number = int(input("Enter a number:"))

c = enter_number * enter_number

a = 1
b = enter_number - 1

combinations = []


while b > 0:
    equation = a*a + b*b

    if b>0 and equation == c:
        combinations.append( (a,b) )
        a += 1
        if a == c:
            a = 0
            b = b - 1
    else: 
        a += 1
        if a == c:
            a = 0
            b = b - 1

if combinations != []:
    print("The following combinations for a and b results in the Pythgorean Theorem for", str(enter_number)+":")
    for i in range(0, len(combinations)):
        print(combinations[i])
else:
    print("There is no Pythgorean Theorem for", enter_number)
