moths_in_house = False
mitch_is_home = True

if moths_in_house and mitch_is_home:
    print("Hoooman! Help me get the moths!")
elif moths_in_house and not mitch_is_home: 
    print("Meoooooooooooooow! Hisssssss!")
elif not moths_in_house and mitch_is_home:
    print("Climb on Mitch.")
elif not moths_in_house and not mitch_is_home:
    print("No threats detected.")