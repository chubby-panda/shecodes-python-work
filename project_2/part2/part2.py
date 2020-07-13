import json
import plotly.express as px
import pandas as pd
from datetime import datetime


with open("data/forecast_10days.json") as json_file:
    json_data = json.load(json_file)

def convert_date(iso_string):
    """Converts an ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')

def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    temp_in_celcius = ((temp_in_farenheit - 32) * 5) / 9
    temp_in_celcius = round(temp_in_celcius, 1)
    return temp_in_celcius

# Define data as list to hold max and min temps/days (as sublists)
data = []
dates = []
min_temps = []
max_temps = []

# Access temps/days and store in sublists in list
for day in json_data["DailyForecasts"]:
    date = convert_date(day["Date"])
    min_temp = convert_f_to_c(day["Temperature"]["Minimum"]["Value"])
    max_temp = convert_f_to_c(day["Temperature"]["Maximum"]["Value"])
    min_real = convert_f_to_c(day["RealFeelTemperature"]["Minimum"]["Value"])
    min_shade = convert_f_to_c(day["RealFeelTemperatureShade"]["Minimum"]["Value"])

    data.append([date, min_temp, max_temp, min_real, min_shade])

# Convert data list to pandas dataframe
df = pd.DataFrame(data, columns=["Date", "Minimum Temperature", "Maximum Temperature", "Minimum Real Feel Temperature", "Minimum Shade Temperature"])

# Produce line graph (min and max)
fig = px.line(df, x="Date", y=["Minimum Temperature", "Maximum Temperature"], labels={"value": "Temperature in Celsius", "variable": "Variables"}, title="Minimum and Maximum Temperatures", hover_name="Date")

fig.show()

# Produce bar chart (min, min real, and min shade)
fig2 = px.bar(df, x="Date", y=["Minimum Temperature", "Minimum Real Feel Temperature", "Minimum Shade Temperature"], labels={"value": "Temperature in Celsius", "variable": "Variables"}, title="Minimum, Minimum Real Feel, and Minimum Shade Temperatures", hover_name="Date")
fig2.update_layout(barmode="group", xaxis_tickangle=-45)

fig2.show()