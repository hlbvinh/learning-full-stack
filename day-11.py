#############################################
############# Functions ####################
###########################################

## Declaring and Calling a Function

# Function without Parameters
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()

# Function Returning a Value - Part 1
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())

# Function with Parameters
    # Single Parameter:

def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

# Two Parameter:

def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age

print('Age: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))


# Passing Arguments with Key and Value
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print(print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh'))

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter


## Function Returning a Value - Part 2
# Returning a string
def print_name(firstname):
    return firstname
print_name('Asabeneh') # Asabeneh

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print_full_name(firstname='Asabeneh', lastname='Yetayeh')

# Returning a number:
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(2019, 1819))

# Returning a boolean
def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False


# Returning a list
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

## Function with Default Parameters
def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))

def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(1821))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon

## Arbitrary Number of Arguments / Số lượng đối số tùy ý
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10

## Default and Arbitrary Number of Parameters in Functions
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))

## Function as a Parameter of Another Function
#You can pass functions around as parameters
def square_number (n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27



#############################################
############# Exercises: Level 1 ###########
###########################################

#1 Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
    return(num1 + num2)
print(add_two_numbers(55,44))

#2 Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(radian):
    pi = 3.14
    return(pi*radian*radian)
print(area_of_circle(4))

#3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    sum_of_list = 0
    for i in nums:
        if type(i) == type(1) or type(i) == type(1.1):
            sum_of_list = sum_of_list + i
        else:
            return("all list items must be number types")
            break 
    return(sum_of_list)             

print(add_all_nums(1,2,3,5))
print(add_all_nums("asdasd",2,3,5))
    

#4 Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(Temperature_oC):
    return((Temperature_oC*9/5) + 32)

print(convert_celsius_to_fahrenheit(30))


#5 Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in [9,10,11]:
        return('Autumn')
    elif month in [12,1,2]:
        return('Winter')
    elif month in [3,4,5]:
        return('Spring')
    else:
        return('Summer')
    
print(check_season(1))

#6 Write a function called calculate_slope which return the slope of a linear equation  => I don't know "the slope of a linear equation"

#7 Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a,b,c):
    delta = b*b - 4*a*c
    if delta < 0:
        return("phương trình vô nghiệm")
    elif delta == 0:
        x = -b/(2*a)
        return(f'Phương trình có nghiệm kép là {x}')
    else:
        x1 = (-b + (b*b - 4*a*c)**0.5)/(2*a)
        x2 = (-b - (b*b - 4*a*c)**0.5)/(2*a)
        return(f'phương trình có 2 nghiệm phân biệt là: x1 = {x1}, x2 = {x2}')

print(solve_quadratic_eqn(2,-5,3))

#8 Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(*lists):
    lts = ""
    for ls in lists:
        lts = lts + ' ' + str(ls)
    return(lts)       

print(print_list(1,'a',2,'b'))

#9 Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
    # print(reverse_list([1, 2, 3, 4, 5]))
    # # [5, 4, 3, 2, 1]
    # print(reverse_list1
    # (["A", "B", "C"]))
    # # ["C", "B", "A"]

def reverse_list(arrs = []):
    list_revert = []
    for i in range(len(arrs)):
        list_revert.append(arrs[len(arrs) - i - 1])
    return(list_revert)

print(reverse_list([1,2,6,'a',4]))

#10 Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(*texts):
    clt = ''
    for text in texts:
        clt = clt + ' ' + str(text).capitalize()
    return(clt)

print(capitalize_list_items('a', 'gAdasdas', 1.1))

#11 Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(list_first=[], *items):
    for item in items:
        list_first.append(item)
    return(list_first)

print(add_item(['ga','vit'],'trau','bo','heo'))



#12 Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
    # food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
    # print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
    # numbers = [2, 3, 7, 9];
    # print(remove_item(numbers, 3))  # [2, 7, 9]

def remove_item(removed_list = [], *items):
    for item in items:
        removed_list.remove(item)
    return(removed_list)

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]


    

#13 Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
    # print(sum_of_numbers(5))  # 15
    # print(sum_of_numbers(10)) # 55
    # print(sum_of_numbers(100)) # 5050

def sum_of_numbers(ranges):
    sum_of_ranges = 0
    for i in range(ranges+1):
        sum_of_ranges = sum_of_ranges + i
    return(sum_of_ranges)

print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

#14 Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(range_odds):
    sum_of_odd = 0
    for i in range(range_odds+1):
        if i % 2 == 1:
            sum_of_odd = sum_of_odd + i
        else:
            pass
    return(sum_of_odd)

print(sum_of_odds(5)) # 1 3 5


#15 Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that range.
def sum_of_even(range_even):
    sum_of_evens = 0
    for i in range(range_even+1):
        if i % 2 == 0:
            sum_of_evens = sum_of_evens + i
        else:
            pass
    return(sum_of_evens)

print(sum_of_even(5)) 


#############################################
############# Exercises: Level 2 ###########
###########################################


#1 Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
    #     print(evens_and_odds(100))
    #     # The number of odds are 50.
    #     # The number of evens are 51.

def evens_and_odds(number):
    count_odds = 0
    count_even = 0
    if type(number) == type(1):
        if number >= 0:
            for i in range(number + 1):
                if i % 2 == 0:
                    count_even = count_even + 1
                else:
                    count_odds = count_odds + 1
            return(f'The number of odds are {count_odds}. \nThe number of even are {count_even}.')
        else:
            return(f'please enter a positive number')
    else:
        return(f'please entern a number')
    
print(evens_and_odds(-1))


#1 Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def giai_thua(number):
    factorial = 1
    if type(number) == type(-1):
        if number < 0:
            for i in range(-number):
                factorial = factorial*(-(i+1))
            return(factorial)
        else:
            for i in range(number):
                factorial = factorial*(i+1)
            return(factorial)
    else:
        return(f'please entern a number')

print(giai_thua('trt'))

#2 Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(param):
    if param:
        return True
    else:
        return False
    
print(is_empty([]))             # True (empty list)
print(is_empty([1, 2, 3]))      # False (non-empty list)
print(is_empty(""))             # True (empty string)
print(is_empty("hello"))        # False (non-empty string)
print(is_empty({}))             # True (empty dictionary)
print(is_empty({"a": 1}))       # False (non-empty dictionary)
print(is_empty(()))             # True (empty tuple)
print(is_empty((1, 2, 3)))      # False (non-empty tuple)
print(is_empty(None))           # True (None)
print(is_empty(0))              # False (non-empty integer)


#3 Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

# what it means?


#############################################
############# Exercises: Level 3 ###########
###########################################

#1 Write a function called is_prime, which checks if a number is prime./ số nguyên tố
def is_prime(positive_number):
    for i in range(positive_number-2):
        if positive_number % (i + 2) == 0:
            return("the number is not prime")
            break
        else:
            continue
    return("the number is prime")

print(is_prime(7))

#2 Write a functions which checks if all items are unique in the list.
def check_unique_item_in_list(list_check = []):
    for i in range(len(list_check)):
        check_item = list_check[i]
        if list_check.count(check_item) > 1:
            return("list is not unique")
        else:
            continue
    return("list is unique")

print(check_unique_item_in_list([1,2,3,4,5,1]))

#3 Write a function which checks if all the items of the list are of the same data type.
def check_item_in_list_same_data_type(list_check = []):
    for i in range(len(list_check) - 1):
        if type(list_check[i]) != type(list_check[(i+1)]):
            return("not same data type")
        else:
            continue
    return("same data type")

print(check_item_in_list_same_data_type([1,2,'r']))


#4 Write a function which check if provided variable is a valid python variable
def is_valid_python_variable(variable):
    """
    Checks if the provided variable name is a valid Python variable name.

    Parameters:
    variable : str
        The variable name to check.

    Returns:
    bool
        True if the variable name is valid, False otherwise.
    """
    # Check if the variable is not empty
    if not variable:
        return False
    
    # Check if the variable starts with a letter or underscore
    if not (variable[0].isalpha() or variable[0] == '_'):
        return False
    
    # Check if the remaining characters are alphanumeric or underscore
    for char in variable[1:]:
        if not (char.isalnum() or char == '_'):
            return False
    
    return True

print(is_valid_python_variable('_asdasdasd'))



#5 Go to the data folder and access the countries-data.py file.
    # Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
    # Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.

import countries_data

def most_spoken_languages():
    print(len(countries_data.countries_data))
    unique_languages = set()
    for country in countries_data.countries_data:
        unique_languages.update(country["languages"])
    #ii
    all_languages = []
    for country in countries_data.countries_data:
        for language in country['languages']:
            all_languages.append(language)

    # Count the occurrences of each language
    language_counts = {}
    for language in all_languages:
        if language in language_counts:
            language_counts[language] += 1
        else:
            language_counts[language] = 1

    most_spoken_languages = []
    for language, count in language_counts.items():
        inserted = False
        for i in range(len(most_spoken_languages)):
            if count > most_spoken_languages[i][1]:
                print(most_spoken_languages[i][1])
                most_spoken_languages.insert(i, (language, count))
                inserted = True
                break
        if not inserted and len(most_spoken_languages) < 10:
            most_spoken_languages.append((language, count))
    str_most = ''   
    print("Ten most spoken languages:")
    for language, count in most_spoken_languages[:10]:
        str_most = str_most + language + ':' + ' ' + str(count) + ' ' + 'contries' + '\n'
    return(str_most)

print(most_spoken_languages())

def most_populated_countries():
    top_population = []
    for popu in countries_data.countries_data:
        inserted = False
        for i in range(len(top_population)):
            if popu['population'] > top_population[i][1]:
                top_population.insert(i, (popu['name'], popu['population']))
                inserted = True
                break
        if not inserted and len(top_population) < 10:
            top_population.append((popu['name'], popu['population']))

    str_pop = 'the 10 most populated countries in the world: '
    for country, number in top_population[:10]:
        str_pop = str_pop + '\n' + country + ':' + ' ' + str(number) + ' people'
    return(str_pop)

print(most_populated_countries())