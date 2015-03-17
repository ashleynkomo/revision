#selection rev 4

number = int(input("Please enter a number between 21 and 29: "))

if 21 <= number <= 29:
    print("this is within range")
elif number < 21:
    print("number is too low")
else:
    print("number is too high")
                   
