import json
import pandas as pd
import plotly.express as px
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

# Functions
def convert_date(iso_string):
    """Converts an ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')


def convert_time(iso_string):
    """Converts an ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    t = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return t.strftime('%H:%M:%S')


# Retrieve JSON data
with open("data/historical_24hours_a.json") as json_file:
    json_data = json.load(json_file)


# Collect temperatures and real feel temperatures and append to list
temperatures = []

hours = 0
day = convert_date(json_data[0]["LocalObservationDateTime"])

for hour in json_data:
    tmp = hour["Temperature"]["Metric"]["Value"]
    rft = hour["RealFeelTemperature"]["Metric"]["Value"]
    temperatures.append([tmp, rft])
    hours += 1


# Create pandas dataframe and box plots
df = pd.DataFrame(temperatures, columns=["Temperature", "Real Feel Temperature"])
fig = px.box(df, y=["Temperature", "Real Feel Temperature"], labels={"value": "Temperature in Celsius", "variable": " "}, title=f"Temperatures / Real Feel Temperatures over {hours} Hours on {day}")

fig.show()


# Collect weather text categories and instances
weather_text_categories = {}

for hour in json_data:
    key = hour["WeatherText"]
    if key not in weather_text_categories.keys():
        weather_text_categories[key] = 1
    elif key in weather_text_categories.keys():
        weather_text_categories[key] += 1

weather_text_categories = list(weather_text_categories.items())


# Create pandas dataframe and bar chart
df2 = pd.DataFrame(weather_text_categories, columns=["Weather Text", "Instances"])
fig2 = px.bar(df2, x="Weather Text", y="Instances", barmode="group", title=f"Weather Text Categories and Instances on {day}")

fig2.show()


# DAY SUMMARY
summary = "------------ SUMMARY OF DAY ------------\n"

# Retrieve min and max temperatures and their times
all_temps = []
all_times = []

for hour in json_data:
    temperature = hour["Temperature"]["Metric"]["Value"]
    all_temps.append(temperature)

    time = hour["LocalObservationDateTime"]
    all_times.append(time)

max_temp = max(all_temps)
max_temp_time = all_times[all_temps.index(max(all_temps))]

min_temp = min(all_temps)
min_temp_time = all_times[all_temps.index(min(all_temps))]

summary = summary + f"The maximum temperature was {max_temp}{DEGREE_SYBMOL} and occurred at {convert_time(max_temp_time)}.\n"
summary = summary + f"The minimum temperature was {min_temp}{DEGREE_SYBMOL} and occurred at {convert_time(min_temp_time)}.\n"
    
# Retrieve amount of precipitation and hours of precipitation

total_hours_precipitation = 0
precipitation_unit = json_data[0]["PrecipitationSummary"]["Past24Hours"]["Metric"]["Unit"]

total_precipitation = 0

for hour in json_data:
    if hour["PrecipitationType"] is not None:
        total_hours_precipitation += 1
    total_precipitation += hour["PrecipitationSummary"]["Past24Hours"]["Metric"]["Value"]

summary = summary + f"The total amount of precipitation over the {hours} hours was {total_precipitation}{precipitation_unit}.\n"
summary = summary + f"Precipitation was recorded for a total of {total_hours_precipitation} out of {hours} hours.\n"

# Retrieve the no. of daylight hours in the last 24 hours
daylight_hours = 0
for hour in json_data:
    if hour["IsDayTime"] is True:
        daylight_hours += 1

summary = summary + f"There were {daylight_hours} hours of daylight in the last {hours} hours.\n"

# Retrieve the max UV index and what hour it occurred
UV_index = []
for hour in json_data:
    UV_index.append(hour["UVIndex"])

max_UV_index = max(UV_index)
max_UV_hour = all_times[UV_index.index(min(UV_index))]

summary = summary + f"The maximum UV index was {max_UV_index} and occurred at {convert_time(max_UV_hour)}."

# Print summary of day
with open("summary_output.txt", "w") as txt_file:
    txt_file.write(summary)