def fah_to_cel(fahrenheit):
    celsius = ((fahrenheit - 32) * 5) / 9
    return celsius

print(fah_to_cel(0))

def cel_to_fah(celsius):
    fahrenheit = ((celsius / 5) * 9) + 32
    return fahrenheit

print(cel_to_fah(0))