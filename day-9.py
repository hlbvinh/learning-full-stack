#############################################
############# Conditionals #################
###########################################

## If Condition
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number
    
## If Else  
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

## If Elif Else
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

## Short Hand
a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed

## Nested Conditions / câu điều kiện lồng nhau
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

## If Condition and Logical Operators
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')    

## If and Or Logical Operators
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')    


###################################################
############# Exercises: Level 1 #################
#################################################

#1 Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. Output:
    # Enter your age: 30
    # You are old enough to learn to drive.
    # Output:
    # Enter your age: 15
    # You need 3 more years to learn to drive.

your_age = int(input("Enter your age: "))
if your_age >= 18:
    print("You are old enough to drive.")
else:
    print(f'You need {18 - your_age} more years to learn to drive.')


#2 Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
    # Enter your age: 30
    # You are 5 years older than me.
my_age = 25
your_age = int(input("nter your age: "))
if (your_age > my_age):
    if (your_age - my_age) > 1:
        print(f'You are {your_age - my_age} years older than me.')
    else:
        print(f'You are 1 year older than me.')
elif (my_age > your_age):
    if (my_age - your_age) > 1:
        print(f'I am {my_age - your_age} years older than you.')
    else:
        print(f'I am 1 year older than you.')
else:
    print("You and I are the same age")


#3 Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, else a is equal to b. Output:
    # Enter number one: 4
    # Enter number two: 3
    # 4 is greater than 3

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is smaller than {b}')
else:
    print(f'{a} is equal to {b}')


###################################################
############# Exercises: Level 2 #################
#################################################

#1 Write a code which gives grade to students according to theirs scores:
    # 80-100, A
    # 70-79, B
    # 60-69, C
    # 50-59, D
    # 0-49, F

student_scores = int(input("student score: "))

if student_scores >= 80:
    print("A")
elif student_scores >= 70:
    print("B")
elif student_scores >= 60:
    print("C")
elif student_scores >= 50:
    print("D")
else:
    print("F")


#2 Check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. 
# March, April or May, the season is Spring June, July or August, the season is Summer

Spring = ['March', 'April', 'May']
Summer = ['June', 'July', 'August']
Autumn = ['September', 'October', 'November']
Winter = ['December', 'January', 'February']

season = input("enter month: ")
if season in Spring:
    print(f'{season} is Spring')
elif season in Summer:
    print(f'{season} is Summer')
elif season in Autumn:
    print(f'{season} is Autumn')
elif season in Winter:
    print(f'{season} is Winter')
else:
    print("invalid value")



#3 The following list contains some fruits:
    # fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
    
fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input("enter fruit name: ")

if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print(fruits)
    



###################################################
############# Exercises: Level 3 #################
#################################################


#1 Here we have a person dictionary. Feel free to modify it!
    #         person={
    #     'first_name': 'Asabeneh',
    #     'last_name': 'Yetayeh',
    #     'age': 250,
    #     'country': 'Finland',
    #     'is_marred': True,
    #     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    #     'address': {
    #         'street': 'Space street',
    #         'zipcode': '02210'
    #     }
    #     }

#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), 
        # if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, 
        # Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#  * If the person is married and if he lives in Finland, print the information in the following format:
    #     Asabeneh Yetayeh lives in Finland. He is married.

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'Node', 'MongoDB'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if person['skills']:
    skills = person['skills']
    mid_ski = skills[len(skills) // 2]
    print(mid_ski)
    # if 'Python' in skills:
    #     print('Python')
    if len(skills) == 2 and 'JavaScript' in skills and 'React' in skills:
        print('He is a front end developer')
    elif 'MongoDB' in skills and 'Node' in skills:
        if 'Python' in skills:
            print('He is a backend developer')
        if 'React' in skills:
            print('He is a fullstack developer')
        else:
            print('unknown title') 
    else:
        print('unknown title')
    



