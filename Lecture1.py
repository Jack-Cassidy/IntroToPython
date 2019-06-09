import re
import math

print("This program allows you to calculate the following:\n a) Area of a circle \n b) Perimeter of a circle \n c) Area of an ellipse \n d) Volume of a cylinder \n e) Square footage of a given house \n f) Conversion of Fahrenheit into Celsius and vice versa")

while True:
    calc = input("Please select an option from 'a' to 'f': ").lower()
    if calc.lower() not in ('a', 'b', 'c', 'd','e','f'):
        print('You have selected an invalid option. Please try again.')
    else:
        break

if calc == 'a':
    while True:
        try:
            radius = float(input('Please enter the radius of your circle in cm: '))
        except ValueError:
            print('You have entered an invalid radius. Please try again.')
            continue
        else:
            break
    area = round(math.pi*radius**2,2)
    print('The area of your cicle is',area,'cm squared')
    
elif calc == 'b':
    while True:
        try:
            radius = float(input('Please enter the radius of your circle in cm: '))
        except ValueError:
            print('You have entered an invalid radius. Please try again.')
            continue
        else:
            break
    perimeter = round(math.pi*radius*2,2)
    print('The perimeter of your circle is',perimeter,'cm')

elif calc == 'c':
    while True:
        try:
            radius1, radius2 = re.split(' ,| |, |,',input('Please enter the two radial values of your ellipse in cm: '))
            radius1,radius2 = float(radius1),float(radius2)
        except ValueError:
            print('You have entered an invalid radius. Please try again.')
            continue
        else:
            break
    area = round(math.pi*radius1*radius2,2)
    print('The area of your ellipse is',area,'cm')
    
elif calc == 'd':
    while True:
        try:
            radius = float(input('Please enter the radius of your cylinder in cm: '))
            #height = float(input('Please enter the height of your cylinder in cm: '))
        except ValueError:
            print('You have entered an invalid radius. Please try again.')
            continue
        else:
            break
    while True:
        try:
            height = float(input('Please enter the height of your cylinder in cm: '))
        except ValueError:
            print('You have entered an invalid height. Please try again.')
            continue
        else:
            break
    volume = round(math.pi*radius**2*height,2)
    print('The volume of your cylinder is',volume,'cm')
    
elif calc == 'e':
    print('This program calculates the area of a house with four rectangular rooms. ')
    while True:
        try:
            length1, width1 = re.split(' ,| |, |,',input('Please enter the two dimensions of your first room in feet: '))
            length1, width1 = float(length1), float(width1)
        except ValueError:
            print('You have entered an invalid value. Please try again.')
            continue
        else:
            break
    while True:
        try:
            length2, width2 = re.split(' ,| |, |,',input('Please enter the two dimensions of your second room in feet: '))
            length2, width2 = float(length2), float(width2)
        except ValueError:
            print('You have entered an invalid value. Please try again.')
            continue
        else:
            break
    while True:
        try:
            length3, width3 = re.split(' ,| |, |,',input('Please enter the two dimensions of your third room in feet: '))
            length3, width3 = float(length3), float(width3)
        except ValueError:
            print('You have entered an invalid value. Please try again.')
            continue
        else:
            break
    while True:
        try:
            length4, width4 = re.split(' ,| |, |,',input('Please enter the two dimensions of your fourth room in feet: '))
            length4, width4 = float(length4), float(width4)
        except ValueError:
            print('You have entered an invalid value. Please try again.')
            continue
        else:
            break
    
    while True:
        calc_volume = input("The program can also calculate the volume of your house, would you like it to? [Yes/No]")
        if calc_volume.lower() not in ('yes','no'):
            print('You have selected an invalid option. Please try again.')
        else:
            break
    if calc_volume.lower() == 'yes':
        while True:
            try:
                height1, height2, height3, height4 = re.split(' ,| |, |,',input('Please enter the height of your four rooms in feet: '))
                height1, height2, height3, height4 = float(height1), float(height2), float(height3), float(height4)
            except ValueError:
                print('You have entered an invalid value. Please try again.')
                continue
            else:
                break
    
    room1_area = round(length1*width1,2)
    room2_area = round(length2*width2,2)
    room3_area = round(length3*width3,2)
    room4_area = round(length4*width4,2)
    
    house_area = room1_area + room2_area + room3_area + room4_area
    
    if calc_volume.lower() == 'yes':
        room1_volume = round(room1_area * height1, 2)
        room2_volume = round(room2_area * height2, 2)
        room3_volume = round(room3_area * height3, 2)
        room4_volume = round(room4_area * height4, 2)
        
        house_volume = room1_volume + room2_volume + room3_volume + room4_volume
        
        print('The square footage of your house is',house_area,'and its total volume is',house_volume,'.')
    else:
        print('The square footage of your house is',house_area,'.')
    
elif calc == 'f':
    while True:
        metric = input("Are you: [a/b] \n a) Converting from Celsius to Fahrenheit \n b) Converting from Fahrenheit to Celsius \n ")
        if metric.lower() not in ('a', 'b'):
            print('You have selected an invalid option. Please try again.')
        else:
            break
    while True:
        try:
            temp = float(input('Please input your starting temperature figure: '))
        except ValueError:
            print('You have entered an invalid temperature. Please try again.')
            continue
        else:
            break
    
    if metric == 'a':
        new_temp = round(temp * (9/5) + 32,2)
        print(str(temp)+'°C is',str(new_temp)+'°F.')
    else:
        new_temp = round((temp - 32) * 5/9,2)
        print(str(temp)+'°F is',str(new_temp)+'°C.')
