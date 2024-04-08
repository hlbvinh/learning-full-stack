#############################################
############# Loops ########################
###########################################

## While Loop

count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4
    
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

# Break and Continue - Part 1
    
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1


## For Loop
# For loop with list

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5

# For loop with string
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])

# For loop with tuple
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# For loop with dictionary Looping through a dictionary gives you the key of the dictionary.
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out


# Loops in set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)  


#@ Break and Continue - Part 2
    # Short reminder: Break: We use break when we like to stop our loop before it is completed.
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break

    # Continue: We use continue when we like to skip some of the steps in the iteration of the loop.
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

## The Range Function
#  syntax: range(start, end, step)

lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

for number in range(11):
    print(number)   # prints 0 to 10, not including 11


## Nested For Loop /vòng lặp lồng nhau
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill) 


# For Else
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)

# Pass / không làm gì cả 
for number in range(6):
    pass



#############################################
############# Exercises: Level 1 ###########
###########################################

#1 Iterate 0 to 10 using for loop, do the same using while loop.
    # for loop
for i in range(11):
    print(i)

i=0
while i <= 10:
    print(i)
    i = i + 1

#2 Iterate 10 to 0 using for loop, do the same using while loop.
for a in range(11):
    print(10 - a)

print("while")
a=11
while a != 0:
    print(a-1)
    a = a - 1

#3 Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#
##
###
####
#####
######
#######
for i in range(1, 8):  # Loop from 1 to 7
    print("#" * i)     # Print '#' repeated i times

i = 1
while i < 8:
    print("#" * i)
    i = i + 1


#4 Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for i in range(4):
    for j in range(2):
        print('# '*8)

for _ in range(8):         # Outer loop for 7 rows
    for _ in range(8):     # Inner loop for 7 columns
        print("#", end=" ")  # Print '#' without newline
    print()                # Move to the next line after printing each row


#5 Print the following pattern:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
    
for i in range(11):
    print(f'{i} x {i} = {i*i}')

#6 Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lit = ['Python', 'Numpy','Pandas','Django', 'Flask']
for nn in lit:
    print(nn)

#7 Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i % 2 == 0:
        print(i)
    pass


#8 Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i % 2 == 1:
        print(i)
    pass


#############################################
############# Exercises: Level 2 ###########
###########################################

#1 Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
import countries

for country in countries.countries:
    if 'land' in country:
        print(country)

#2 This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
frut = ['banana', 'orange', 'mango', 'lemon']
i = 4
for fr in frut:
    frut.pop(0)
    frut.insert(len(frut) - i, fr)
    i = i + 1
    print(frut)

#3 Go to the data folder and use the countries_data.py file.
    #i What are the total number of languages in the data
    #ii Find the ten most spoken languages from the data
    #iii Find the 10 most populated countries in the world

#i 
import countries_data
print(len(countries_data.countries_data))

unique_languages = set()
for country in countries_data.countries_data:
    unique_languages.update(country["languages"])

# Total number of languages
total_languages = len(unique_languages)
print("Total number of languages:", total_languages)

#ii
all_languages = []
for country in countries_data.countries_data:
    for language in country['languages']:
        all_languages.append(language)

count_languages = []
for language in unique_languages:
    count_nn = all_languages.count(language)
    count_languages.append(count_nn)

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
    
print("Ten most spoken languages:")
for language, count in most_spoken_languages[:10]:
    print(f"{language}: {count} countries")

#iii Find the 10 most populated countries in the world
# population
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

print("the 10 most populated countries in the world: ")
for country, number in top_population[:10]:
    print(f"{country}: {number} people")