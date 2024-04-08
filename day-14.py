#####################################################
############# Higher Order Functions ###############
###################################################

# In Python functions are treated as first class citizens, allowing you to perform the following operations on functions:

# A function can take one or more functions as parameters
# A function can be returned as a result of another function
# A function can be modified
# A function can be assigned to a variable
# In this section, we will cover:

# Handling functions as parameters
# Returning functions as return value from another functions
# Using Python closures and decorators

## Function as a Parameter
def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15

## Function as a Return Value
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3

## Python Closures / function lồng function
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20

## Python Decorators
# Creating Decorators
# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator

'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON


# Applying Multiple Decorators to a Single Function


'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

# Accepting Parameters in Decorator Functions
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')

### Built-in Higher Order Functions

## Python - Map Function
    # syntax
    # map(function, iterable)
# Example:1

numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]


# Example:2

numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]


# Example:3

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Let us apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']



## Python - Filter Function
    # syntax
    # filter(function, iterable)

# Example:1

# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]


# Example:2

numbers = [1, 2, 3, 4, 5]  # iterable

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]

# Example 3

# Filter long name
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['Asabeneh']


# Python - Reduce Function

# Example:1
from functools import reduce

numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15



################################################
############# Exercises: Day 14 ###############
##############################################

########################################
######### Exercises: Level 1 ##########
######################################

#1 Explain the difference between map, filter, and reduce.
    # map trả vè list ( dùng list để in ra mới đc)
    # filter trả về true/false
    # reduce trả về single value


#2 Explain the difference between higher order function, closure and decorator

#3 Define a call function before map, filter or reduce, see examples.

# Example:1

numbers = [1, 2, 3, 4, 5] # iterable
def square(ite=[]):
    return_list = []
    for i in ite:
        return_list.append(i**2)
    return return_list

print(square(numbers))

# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    return_list=[]
    for i in num:
        if i % 2 == 0:
            return_list.append(i)
        else:
            continue
    return return_list

print(is_even(numbers))

# reduce
from functools import reduce

numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x):
    sum = 0
    for i in x:
        sum = sum + int(i)
    return sum

print(add_two_nums(numbers_str))

#4 Use for loop to print each country in the countries list.

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for i in countries:
    print(i)

#5 Use for to print each name in the names list.
for i in names:
    print(i)  

#6 Use for to print each number in the numbers list.
for i in numbers:
    print(i)


########################################
######### Exercises: Level 2 ##########
######################################
    
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#1 Use map to create a new list by changing each country to uppercase in the countries list
def upper_case_country(country):
    return country.upper()

list_upper_case_country = map(upper_case_country, countries)
print(list(list_upper_case_country))


#2 Use map to create a new list by changing each number to its square in the numbers list
print(list(map(lambda x: x**2, numbers)))


#3 Use map to change each name to uppercase in the names list
print(list(map(lambda name: name.upper(), names)))

#4 Use filter to filter out countries containing 'land'.
print(list(filter(lambda country: 'land' in country, countries)))

#5 Use filter to filter out countries having exactly six characters.
print(list(filter(lambda country: len(country)==6,countries)))

#6 Use filter to filter out countries containing six letters and more in the country list.
print(list(filter(lambda country: len(country)>=6,countries)))

#7 Use filter to filter out countries starting with an 'E'
print(list(filter(lambda country: country[0]=='E',countries)))

#8 Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce

# Danh sách các số
numbers = [1, 2, 3, 4, 5, 6]

# Chuỗi các phương thức xử lý
result = reduce(lambda acc, x: acc + x, filter(lambda x: x % 2 == 0, map(lambda x: x * x, numbers)))

print(result)  # Kết quả sẽ là tổng bình phương của các số chẵn trong danh sách: 4 + 16 + 36

#9 Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lis=[]):
    list_return=[]
    for i in range(len(lis)):
        list_return.insert(i,str(lis[i])) 
    return list_return

print(get_string_lists([234234,2,3,4]))

#10 Use reduce to sum all the numbers in the numbers list.
from functools import reduce

numbers_str = [1,2,3,4,5,6,7]  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15


#11 Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
def concatenate_all_countries(x,y):
    return str(x) + ',' + ' ' + str(y)

print(reduce(concatenate_all_countries, countries))


#12 Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
def categorize_countries(countries = []):
    list_return = []
    for i in countries:
        if 'land' in i:
            list_return.append(i)
        else:
            continue
    return list_return

import countries

print(categorize_countries(countries.countries))


#13 Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def count_countries_starting_with_letters(country_names):
    # Initialize an empty dictionary to store the counts
    letter_counts = {}

    # Iterate through each country name
    for country in country_names:
        # Get the first letter of the country name
        first_letter = country[0].upper()

        # Increment the count for the letter or initialize it to 1 if it doesn't exist
        letter_counts[first_letter] = letter_counts.get(first_letter, 0) + 1

    return letter_counts

print(count_countries_starting_with_letters(countries.countries))



#14 Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries(countries):
    return_list = []
    for i in range(10):
        return_list.append(countries[i])
    return return_list

print(get_first_ten_countries(countries.countries))

#15 Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(countries):
    return_list = []
    for i in range(10):
        return_list.append(countries[i-10])
    return return_list

print(get_last_ten_countries(countries.countries))

########################################
######### Exercises: Level 3 ##########
######################################

#1 Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
    # Sort countries by name, by capital, by population
    # Sort out the ten most spoken languages by location.
    # Sort out the ten most populated countries.













