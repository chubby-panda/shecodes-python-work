# Import csv module (to read csv file)
import csv

# Create empty list for colours
colors = []

# Import csv file, read and copy to list
with open("colours_213.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colors.append(line)

# Empty list for colour count
red = 0
green = 0
blue = 0

# Iterate through list and add 1 for each occurence
for color in colors:
    if "red" in color[4]:
        red += 1
    if "green" in color[4]:
        green += 1
    if "blue" in color[4]:
        blue += 1

# Print results
print(f"Red: {red}")
print(f"Green: {green}")
print(f"Blue: {blue}")