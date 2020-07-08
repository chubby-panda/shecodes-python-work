import json
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and 'degrees celcius.'
    """
    temp = float(temp)
    return f"{temp:.1f}{DEGREE_SYBMOL}"

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


def calculate_mean(total, num_items):
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    mean = total / num_items
    if type(mean) == float:
        return round(mean, 1)
    elif type(mean) == int:
        return mean


def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    with open(forecast_file) as json_file:
        json_data = json.load(json_file)

    # Create empty variable to store output
    forecast_data = f""

    # Create empty lists to store temps in C for summary
    min_temps = {}
    max_temps = {}

    for day in json_data["DailyForecasts"]:
        # Get Date
        date = convert_date(day["Date"])
        forecast_data += f"\n-------- {date} --------\n"

        # Get Minimum Temperature
        min_temp = convert_f_to_c(day["Temperature"]["Minimum"]["Value"])
        min_temps.update({date: min_temp})
        min_temp = format_temperature(min_temp)
        min_temp_string = "Minimum Temperature:"
        forecast_data += f"{min_temp_string:<21}{min_temp}\n"

        # Get Maximum Temperature
        max_temp = convert_f_to_c(day["Temperature"]["Maximum"]["Value"])
        max_temps.update({date: max_temp})        
        max_temp = format_temperature(max_temp)
        max_temp_string = "Maximum Temperature:"
        forecast_data += f"{max_temp_string:<21}{max_temp}\n"

        # Get Daytime Long Phrase
        daytime = day["Day"]["LongPhrase"]
        forecast_data += f"Daytime: {daytime}\n"

        # Get Daytime Chance of Rain
        rain_chance_day = day["Day"]["RainProbability"]
        rain_chance_day = str(rain_chance_day) + "%"
        rain_chance_day_string = "    Chance of rain:"
        forecast_data += f"{rain_chance_day_string:<21}{rain_chance_day}\n"

        # Get Nighttime Long Phrase
        nighttime = day["Night"]["LongPhrase"]
        forecast_data += f"Nighttime: {nighttime}\n"

        # Get Nighttime Chance of Rain
        rain_chance_night = day["Night"]["RainProbability"]
        rain_chance_night = str(rain_chance_night) + "%"
        rain_chance_night_string = "    Chance of rain:"
        forecast_data += f"{rain_chance_night_string:<21}{rain_chance_night}\n"

    # Get the average high
    max_temps_total = 0
    max_temps_days = 0
    for days, temps in max_temps.items():
        max_temps_total += temps
        max_temps_days += 1
    average_high = calculate_mean(max_temps_total, max_temps_days)
    average_high = format_temperature(average_high)
    forecast_data = f"    The average high this week is {average_high}.\n" + forecast_data
        
    # Get the average low
    min_temps_total = 0
    min_temps_days = 0
    for days, temps in min_temps.items():
        min_temps_total += temps
        min_temps_days += 1
    average_low = calculate_mean(min_temps_total, min_temps_days)
    average_low = format_temperature(average_low)
    forecast_data = f"    The average low this week is {average_low}.\n" + forecast_data

    # Get the highest temperature for summary
    highest_temp = max(max_temps.values())
    highest_day = [day for day in max_temps if max_temps[day] == highest_temp][0]
    highest_temp = format_temperature(highest_temp)
    forecast_data = f"    The highest temperature will be {highest_temp}, and will occur on {highest_day}.\n" + forecast_data

    # Get the lowest temperature for summary
    lowest_temp = min(min_temps.values())
    lowest_day = [day for day in min_temps if min_temps[day] == lowest_temp][0]
    lowest_temp = format_temperature(lowest_temp)
    forecast_data = f"    The lowest temperature will be {lowest_temp}, and will occur on {lowest_day}.\n" + forecast_data

    # Get number of days - overview
    num_days = len(json_data["DailyForecasts"])
    forecast_data = f"{num_days} Day Overview\n" + forecast_data

    # Add an extra new line at the end
    forecast_data += "\n"
    # Final Return Statement
    return forecast_data
            

if __name__ == "__main__":
    print(process_weather("data/forecast_5days_b.json"))





