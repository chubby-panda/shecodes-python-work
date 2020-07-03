print("This is a simple program to calculate a series of numbers. Enter a number to add to the sum, and when you are ready to see the result enter a single space.")

sum = 0
run_program = True

while run_program:
    number = input("Enter a number: ")
    if number == " ":
        run_program = False
    else:
        number = int(number)
        sum += number

print(sum)