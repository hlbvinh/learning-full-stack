#################$##############################
############## TUPLES #########################
#################$############################

# A tuple is a collection of different data types which is ordered and unchangeable (immutable). Tuples are written with round brackets, (). 
# Once a tuple is created, we cannot change its values. We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable).
# Unlike list, tuple has few methods. Methods related to tuples:
# tuple(): to create an empty tuple
# count(): to count the number of a specified item in a tuple
# index(): to find the index of a specified item in a tuple
# operator: to join two or more tuples and to create a new tuple

## Creating a Tuple
# Empty tuple: Creating an empty tuple
# syntax
empty_tuple = ()
print(empty_tuple)
# or using the tuple constructor
empty_tuple = tuple()
print(empty_tuple)

# Tuple with initial values
tpl = ('item1', 'item2','item3')
fruits = ('banana', 'orange', 'mango', 'lemon')
list(fruits)
print(list(fruits))

print(tpl)
print(fruits)

## Tuple length

print(len(tpl))
print(len(fruits))

## Accessing Tuple Items
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]

## Slicing tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]

print(orange_mango)


## Changing Tuples to Lists
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')


## Checking an Item in a Tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
#fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignments

## Joining Tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables

print(fruits_and_vegetables)

## Deleting Tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits

#############################################
############# Exercises: Level 1 ###########
###########################################

#1 Create an empty tuple
emty_tp1 = ()
emty_tp2 = tuple()
print(emty_tp1)
print(emty_tp2)

#2 Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
my_sis = ('Thuong', 'Trinh')
my_bro = ('Tin', 'Duan', 'Quan', 'Boom', 'Buoi', 'Bong', 'Bin')

#3 Join brothers and sisters tuples and assign it to siblings
siblings = my_sis + my_bro
print(siblings)

#4 How many siblings do you have? => Many :D

#5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members 
family_members = siblings + ('David', 'Mery')
print(family_members)

#############################################
############# Exercises: Level 2 ###########
###########################################

#1 Unpack siblings and parents from family_members
siblings = family_members[:-2]
my_parents = family_members[-2:]
print(siblings)
print(my_parents)

#2 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('chuoi', 'oi')
vegetables = ('ca rot', 'dau xanh')
animal = ('ho', 'trau')
food_stuff_tp = fruits + vegetables + animal

#3 Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

#4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff_tp_first = food_stuff_tp[:(len(food_stuff_tp)//2)]
food_stuff_tp_last = food_stuff_tp[(len(food_stuff_tp)//2):]

#5 Slice out the first three items and the last three items from food_staff_lt list
food_stuff_lt_first = food_stuff_lt[0:3]
food_stuff_lt_last = food_stuff_lt[-3:]
print(food_stuff_lt_first)
print(food_stuff_lt_last)

#6 Delete the food_staff_tp tuple completely
del food_stuff_tp

#7 Check if an item exists in tuple:
    # Check if 'Estonia' is a nordic country
    # Check if 'Iceland' is a nordic country
    # nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)




# Tuple with initial values
string1 = 'habsdkbkasd'
print(string1[:3])
