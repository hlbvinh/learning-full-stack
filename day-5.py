                #####  LIST   #####
                ###################

### How to Create a List

# syntax 
list = list()
#or
list_1 = []

# Lists with initial values
fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and its length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))

# Lists can have items of different data types
lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types

print(lst)

#### Accessing List Items Using Positive Indexing
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]


# Accessing List Items Using Negative Indexing

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango


# Unpacking List Items
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

# First Example
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits 
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
# Third Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)


### Sicing Items from a List
#Positive Indexing: We can specify a range of positive indexes by specifying the start, end and step, the return value will be a new list. 
#default values for start = 0, end = len(lst) - 1 (last item), step = 1)

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']

# Negative Indexing: We can specify a range of negative indexes by specifying the start, end and step, the return value will be a new list.
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']

##Modifying Lists

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']


### Checking Items in a List
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

# Adding Items to a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)

# Inserting Items into a List
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)

### Removing Items from a List
# The remove method removes a specified item from a list
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']

# Removing Items Using Pop
# The pop() method removes the specified index, (or the last item if index is not specified):
# syntax
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']

## Removing Items Using Del
# The del keyword removes the specified index and it can also be used to delete items within index range. It can also delete the list completely
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)       # ['orange', 'lime']
del fruits
#print(fruits)       # This should give: NameError: name 'fruits' is not defined

## Clearing List Items
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []

## Copying a List

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']

## Joining Lists
# Plus Operator (+)
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables ) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

## Joining using extend() method The extend() method allows to append list in a list
num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1) # Numbers: [0, 1, 2, 3, 4, 5, 6]
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers) # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits ) # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

## Counting Items in a List
#The count() method returns the number of times an item appears in a list
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3


## Finding Index of an Item
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, the first occurrence


## Reversing a List / đảo ngược list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) # [24, 25, 24, 26, 25, 24, 19, 22]

## Sorting List Items
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)             # sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)
print(fruits) # ['orange', 'mango', 'lemon', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]

ages.sort(reverse=True)
print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]

# sorted(): returns the ordered list without modifying the original list
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
# Reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits,reverse=True)
print(fruits)     # ['orange', 'mango', 'lemon', 'banana']

################################################
########## Exercises: Day 5 ###################
##############################################
# 1 Declare an empty list
List = []

# 2 Declare a list with more than 5 items
car = ['mec', 'audi', 'toyota', 'marda', 'rr', 'suzuki']
print(car)

# 3 Find the length of your list
print(len(car))

# 4 Get the first item, the middle item and the last item of the list
print(car[0])
print(car[-1])
print(car[(len(car) - 1)//2])

# 5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Vinh', 26, 1.7, 'single', 'HCM']

# 6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7 Print the list using print()
print(it_companies,'\n',mixed_data_types)

# 8 Print the number of companies in the list
print(len(it_companies))

# 9 Print the first, middle and last company
print(it_companies[0])
print(it_companies[-1])
print(it_companies[(len(it_companies) - 1)//2])

# 10 Print the list after modifying one of the companies
it_companies[0] = "youtube"
print(it_companies)

# 11 Add an IT company to it_companies
it_companies.append('TMA')
print(it_companies)

# 12 Insert an IT company in the middle of the companies list
it_companies.insert(4,'SHOPPE')
print(it_companies)


# 13 Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
print(it_companies)


# 14 Join the it_companies with a string '#;  '
string1 = "#;  "
it_companies.extend([string1])
print(it_companies)

# 15 Check if a certain company exists in the it_companies list.
print('Google' in it_companies)
print('asdasd' in it_companies)

# 16 Sort the list using sort() method
it_companies.sort()
print(it_companies)

# 17 Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)


# 18 Slice out the first 3 companies from the list
print(it_companies[0:3])

# 19 Slice out the last 3 companies from the list
print(it_companies[-4:-1])

# 20 Slice out the middle IT company or companies from the list
print(it_companies[2:6])

# 21 Remove the first IT company from the list
del it_companies[0]
print(it_companies)

# 22 Remove the middle IT company or companies from the list
it_companies.remove('IBM')
print(it_companies)

# 23 Remove the last IT company from the list
del it_companies[-1]
print(it_companies)

# 24 Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# 25 Destroy the IT companies list
del it_companies
#print(it_companies)


# 26 Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)

# 27 After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux
full_stack = front_end.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)


###################################
############ Exercises: Level 2 #######
###########################################

# 1 .The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print(ages)
print("min is: ", ages[0])
print("max is: ", ages[-1])

# Add the min age and the max age again to the list
ages.append(ages[0])
ages.append(ages[len(ages) - 2])
print(ages)

# Find the median age (one middle item or two middle items divided by two)
ages.sort()
print(ages[(len(ages) -1)//2])
print(ages[len(ages)//2])

# Find the average age (sum of all items divided by their number )
ave = sum(ages)/len(ages)
print(ave)

# Find the range of the ages (max minus min)
ages.sort()
range = ages[-1] - ages[0]
print(range)

# Compare the value of (min - average) and (max - average), use abs() method
min_ave = abs(ages[0] - ave)
max_ave = abs(ages[-1] - ave)

print(min_ave > max_ave)

# 2 Find the middle country(ies) in the
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
print(countries[len(countries) // 2])
print(countries[(len(countries)+1) // 2])

# 3 Divide the countries list into two equal lists if it is even if not one more country for the first half.

countries_1 = countries[0:len(countries) // 2]
print(countries_1)
countries_2 = countries[len(countries) // 2: len(countries) -1]
print(countries_1)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries

list1= ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
cn, ru, us, *scan = list1
print(cn)
print(ru)
print(us)
print(*scan)

























