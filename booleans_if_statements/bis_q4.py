height_prompt = "How tall are you in cms? "
height = input(height_prompt)
height = int(height)

if height >= 120:
    print("Hop on!")
else:
    print("Sorry, not today :(")