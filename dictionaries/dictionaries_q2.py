# Names to be transferred
names = [
    "Maddy", "Bel", "Elnaz", "Gia", "Izzy", "Joy", "Katie", "Maddie", "Tash", "Nic", "Rachael", "Bec", "Bec", "Tabitha", "Teagen", "Viv", "Anna", "Catherine", "Catherine", "Debby", "Gab", "Megan", "Michelle", "Nic", "Roxy", "Samara", "Sasha", "Sophie", "Teagen", "Viv"
]

# Names that have been entered into the dictionary already
listed_names = []

# The dictionary of names
names_dictionary = {}

# Iterate through names
for name in names:
    # Check if name has been entered and update
    if name not in listed_names:
        names_dictionary.update({name: 1})
        listed_names.append(name)
    elif name in listed_names:
        names_dictionary[name] += 1

# Print names dictionary
for name, times in names_dictionary.items():
    print(f"{name} {times}")