#############################################
############# Modules ######################
###########################################

## What is a Module?
# Creating a Module
# Importing a Module

import mymodules

print(mymodules.generate_full_name('vinh', 'huynh'))

# Import Functions from a Module
# main.py file
from mymodules import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Asabneh','Yetayeh'))
print(sum_two_nums(1,9))
mass = 100
weight = mass * gravity
print(weight)
print(person['firstname'])

# Import Functions from a Module and Renaming
# main.py file
from mymodules import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100
weight = mass * g
print(weight)
print(p)
print(p['firstname'])

## Import Built-in Modules
# OS Module
# import the module
import os
# Creating a directory
os.mkdir('./directory_name')
# Changing the current directory
os.chdir('./')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir('./directory_name')

# Sys Module
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2 / arg thông số truyền vào khi chạy script
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

# # To know the largest integer variable it takes
# sys.maxsize
# # To know environment path
# sys.path
# # To know the version of python you are using
# sys.version
# # to exit sys
# sys.exit()

## Statistics Module
from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3

## Math Module
import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base

from math import pi
print(pi)

#  import multiple functions at once

from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2

# import all the function in math module
from math import *
print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(math.log10(100))     # 2

## String Module
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

## Random Module
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive



##############################################
############# Exercises: Level 1 ############
############################################

#1 Write a function which generates a six digit/character random_user_id.
    #   print(random_user_id());
    #   '1ee33d'
import random
import string
def random_user_id():
    random_id = ''.join(random.choices(string.ascii_letters + string.digits, k = 6))
    return(random_id)

print(random_user_id())

#2 Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
    # print(user_id_gen_by_user()) # user input: 5 5
    # #output:
    # #kcsy2
    # #SMFYb
    # #bWmeq
    # #ZXOYh
    # #2Rgxf
    
    # print(user_id_gen_by_user()) # 16 5
    # #1GCSgPLMaBAVQZ26
    # #YD7eFwNQKNs7qXaT
    # #ycArC5yrRupyG00S
    # #UbGxOFI7UXSWAyKN
    # #dIV0SSUTgAdKwStr

def user_id_gen_by_user():
    number_of_characters = input("Enter the number of characters: ")
    number_of_ids = input("Enter the number of IDs: ")
    random_id = ''
    for i in range(int(number_of_ids)):
        random_id = random_id + ''.join(random.choices(string.ascii_letters + string.digits, k = int(number_of_characters))) + '\n'
    return(random_id)

print(user_id_gen_by_user());   

#3 Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
    # print(rgb_color_gen())
    # # rgb(125,244,255) - the output should be in this form
def rgb_color_gen():
    color_r = randint(0,255)
    color_g = randint(0,255)
    color_b = randint(0,255)
    return(f'rgb({color_r},{color_g},{color_b})')

print(rgb_color_gen())

##############################################
############# Exercises: Level 2 ############
############################################

#1 Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
def list_of_hexa_colors(num):
    color = []
    for i in range(num):
        hex_number = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        color.append(hex_number)
    return(color)

print(list_of_hexa_colors(3))

#2 Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

def rgb_color_gen(num):
    color = []
    for i in range(num):
        color_r = randint(0,255)
        color_g = randint(0,255)
        color_b = randint(0,255)
        color.append(f'rgb({color_r},{color_g},{color_b})')
    return(color)

print(rgb_color_gen(3))

#3 Write a function generate_colors which can generate any number of hexa or rgb colors.
    #    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
    #    generate_colors('hexa', 1) # ['#b334ef']
    #    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
    #    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']

def generate_colors(hexa_or_rgb, num):
    if hexa_or_rgb == 'hexa':
        print(list_of_hexa_colors(num))
    elif hexa_or_rgb == 'rgb':
        print(rgb_color_gen(num))
    else:
        print('invalid parameter')
    
generate_colors('hexa', 3)
generate_colors('hexa', 1)
generate_colors('rgb', 3)
generate_colors('rgb', 1)

##############################################
############# Exercises: Level 3 ############
############################################

#1 Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

def shuffle_list(list_input = []):
    random.shuffle(list_input)
    return(list_input)

print(shuffle_list([1,'a',2,3,'d','ra']))


#2 Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

def array_of_7_nums_unique():
    arr_7_uni = []
    convert_str = ''
    while len(arr_7_uni) < 7:
        num = randint(0,9)
        convert_str = ''.join(str(x) for x in arr_7_uni)
        if convert_str.find(str(num)) == -1:
            arr_7_uni.append(num)
        else:
            continue
    return(arr_7_uni)

print(array_of_7_nums_unique())

