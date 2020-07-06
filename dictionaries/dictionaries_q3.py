# Import module to read csv
import csv

colours = []

# Define a function that reads a csv and converts to list
def read_csv_file(filepath):
    with open(filepath) as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            colours.append(line)
        return colours

read_csv_file("colours_20.csv")

colour_glossary = []
labels = colours.pop(0)

# Define a function to convert list to dictionary
def convert_to_dictionary(list):
    i = 0
    dictionary = {}
    while i < len(list):
        dictionary.update({labels[i]: list[i]})
        i += 1
    colour_glossary.append(dictionary)

for colour in colours:
    convert_to_dictionary(colour)

print(colour_glossary[1])