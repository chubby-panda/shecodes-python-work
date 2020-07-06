# Import module to read csv
import csv

# Define an empty list 
colours = []

# Define a function that reads a csv and converts to list
def read_csv_file(filepath):
    with open(filepath) as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            colours.append(line)
        return colours

# Define a function that formats the output by line
def format_colour_line(colour_data):
    colour_data[1] = colour_data[1].strip()
    colour_data[2] = colour_data[2].strip()
    colour_data[4] = colour_data[4].strip()
    rgb = f"{colour_data[1]:<18}"
    hex = f"{colour_data[2]:<18}"
    name = f"{colour_data[4]:<18}"
    return f"{rgb}{hex}{name}"


# Call the function to read the file and convert to list
read_csv_file("colours_213.csv")

# Call the function to format the output, and print
for line in colours:
    line = format_colour_line(line)
    print(line)