def calculate_mean(total_sum, num_items):
    mean = total_sum / num_items
    return mean

total = 0
counter = 0
run_program = True

print("Enter numbers to calculate mean. Enter space when finished.")

while run_program:
    number = input("Enter a number: ")
    if number == " ":
        result = calculate_mean(total, counter)
        print(f"The mean is: {result}")
        run_program = False
    else:
        number = float(number)
        total += number
        counter += 1
