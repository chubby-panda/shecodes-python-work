# Import csv module (to read csv file)
import csv

# Create empty list for colours
colors = []

# Import csv file, read and copy to list
with open("colours_20.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colors.append(line)

# Iterate through lines / format and print output
for color in colors:
    color[1] = color[1].strip()
    color[2] = color[2].strip()
    color[4] = color[4].strip()
    rgb = f"{color[1]:<18}"
    hex = f"{color[2]:<18}"
    name = f"{color[4]:<18}"
    print(f"{rgb}{hex}{name}")