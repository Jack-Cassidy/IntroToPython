print("This program allows you to calculate the following:\n a) Area of a circle \n b) Perimeter of a circle \n c) Area of an ellipse \n d) Volume of a cylinder \n e) Square footage of a given house \n f) Conversion of Fahrenheit into Celsius and vice versa")

while True:
	calc = input("Please select an option from 'a' to 'f': ")
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
		except ValueError:
			print('You have entered an invalid radius. Please try again.')
			continue
		else:
			break
	area = round(math.pi*float(radius1)*float(radius2))
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
	print('This program calculates the area of a house with four ractangular rooms. ')
	while True:
		try:
			height1, width1 = re.split(' ,| |, |,',input('Please enter the two dimensions of your first room in feet: '))
		except ValueError:
			print('You have entered an invalid value. Please try again.')
			continue
		else:
			break
	while True:
		try:
			height2, width2 = re.split(' ,| |, |,',input('Please enter the two dimensions of your second room in feet: '))
		except ValueError:
			print('You have entered an invalid value. Please try again.')
			continue
		else:
			break
	while True:
		try:
			height3, width3 = re.split(' ,| |, |,',input('Please enter the two dimensions of your third room in feet: '))
		except ValueError:
			print('You have entered an invalid value. Please try again.')
			continue
		else:
			break
	while True:
		try:
			height4, width4 = re.split(' ,| |, |,',input('Please enter the two dimensions of your fourth room in feet: '))
		except ValueError:
			print('You have entered an invalid value. Please try again.')
			continue
		else:
			break
	
	while True:
		calc_volume = input("The program can also calculate the volume of your house, would you like it to? [Yes/No]")
		if calc_volume.lower() not in ('yes','no'):
			print('You have selected an invalid option. Please try again.')
		elif calc_volume.lower() == 'yes':
			height1, height2, height3, height4 = re.split(' ,| |, |,',input('Please enter the height of your four rooms in feet: '))
			break
		else:
			break
	
	room1_area = round(float(height1)*float(width1),2)
	room2_area = round(float(height2)*float(width2),2)
	room3_area = round(float(height3)*float(width3),2)
	room4_area = round(float(height4)*float(width4),2)
	
	room1_volume = room1_area * float(height1)
	room2_volume = room2_area * float(height2)
	room3_volume = room3_area * float(height3)
	room4_volume = room4_area * float(height4)
	
	house_area = room1_area + room2_area + room3_area + room4_area
	house_volume = room1_volume + room2_volume + room3_volume + room4_volume
	
	if calc_volume.lower() == 'yes':
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