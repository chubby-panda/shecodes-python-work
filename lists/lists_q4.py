my_string = input("Please enter a string (sentence): ")

words = my_string.split()
print(f"{len(words)} {words}")

letters = list(my_string)
print(f"{len(letters)} {letters}")