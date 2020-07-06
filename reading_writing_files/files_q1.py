names = []

with open("names.txt") as txt_file:
    for name in txt_file:
        name = name.strip()
        names.append(name)

for counter, name in enumerate(names, 1):
    print(f"{counter}. {name}")