#!/usr/bin/env python
# coding: utf-8

# In[12]:


import math
from math import pi as pi
import random as r

#Question 1: Shape Area Functions

def circle(radius):
    area = pi * radius**2
    return round(area,2)

def cylinder(radius, height):
    volume = radius**2*height*pi
    return round(volume,2)

cylinder(4,5)

def cone(radius, height):
    volume = pi*radius**2*height/3
    return round(volume,2)

cone(4,9)


# In[7]:


#Question 2: Recursive User Input

def ask_for_value():
    val = input("Enter a value: ")
    try:
        val = float(val)
    except:
        return ask_for_value()
    else:
        return val
        

def menu():
    option = input("Please choose an option from 1-3: \n 1. Calculate the area of a circle.\n 2. Calculate the volume of a cylinder.\n 3. Calculate the volume of a cone.\n You have selected: ")
    try:
        option = float(option)
    except:
        print("Invalid option.")
        return menu()  
    else:
        if int(option) not in [1,2,3]:
            print("Invalid option.")
            menu()
        elif option == 1:
            print("Please enter the radius of your circle. ")
            radius = ask_for_value()
            print(circle(radius))
        elif option == 2:
            print("Please enter the radius of your cylinder. ")
            radius = ask_for_value()
            print("Please enter the height of your cylinder. ")
            height = ask_for_value()
            print(cylinder(radius, height))
        elif option == 3:
            print("Please enter the radius of your cone. ")
            radius = ask_for_value()
            print("Please enter the height of your cone. ")
            height = ask_for_value()
            print(cone(radius, height))

menu()
    


# In[19]:


#Question 3 - 

from datafile import data

# Initialise variables.

# Define functions.
def show_raw_data(dat):
   for ind in range(0, len(data), 2):
       print(dat[ind].ljust(10), str(dat[ind + 1]).rjust(4)) 

# Main body of program.
show_raw_data(data)

def pass_list():

    names = data[0::2]
    grades = data[1::2]
    classification = []
    
    i = 0
    
    while i <= len(grades)-1:
        for grade in grades:
            if grade >= 70:
                classification.append("Distinction")
            elif grade >= 60:
                classification.append("")


# In[56]:


#Question 4 - Rucksack

def adventure_game():
    rucksack = ["Water flask", 
                "Cheese", 
                "Gold Coins", 
                "Hankerchief", 
                "Tinderbox", 
                "Scrolls", 
                "Dagger", 
                "Rope", 
                "Nuts", 
                "Pipe", 
                "Tobacco", 
                "Herbs", 
                "Wineskin", 
                "Axe"]
    rucksack.sort()
    print(rucksack)

    print(len(rucksack))
    
    rucksack.append("Gems")
    rucksack.append("Necklace")
    print(rucksack)
    
    rucksack.sort()
    print(rucksack)
    
    
    f = 5
    while f > 0:
        i = r.randint(0,len(rucksack)-1)
        del rucksack[i]
        #print(len(rucksack))
        f -= 1
    print(rucksack)
    
adventure_game()


# In[93]:


#Question 5 - Dice Roll

def dice_roll(rolls):
    print("This program tallies the results of throwing two dice as many times as you select.")
    
    results = []
    
    while rolls > 0:
          
        dice1 = r.randint(1,6)
        dice2 = r.randint(1,6)
        total = dice1 + dice2
        #print(total)
        
        results.append(total)

        results_dict = dict((x,results.count(x)) for x in set(results))
          
        rolls -= 1
        
    print(results_dict)
    print("Distribution Chart\nScore Rolls")
    for i in results_dict:
        print(i, results_dict[i],'*'*results_dict[i])
    
dice_roll(100)


# In[ ]:





# In[ ]:





# In[ ]:




