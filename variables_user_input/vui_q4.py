name_prompt = "What is your name? "
height_prompt = "How tall are you in cms? "

name = input(name_prompt)
height = input(height_prompt)

name = name.title()

print(f"{name} is {height}cm tall.")