number = input(
    "Please provide a number and I'll tell you if it is a multiple of 10: "
    )
number = int(number)

if number % 10 == 0:
    print("Your number is a multiple of 10")
else:
    print("Your number is not a multple of 10")
