#############################################
############# Dictionaries #################
###########################################

# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

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

print(person['address'])

# Dictionary Length
print(len(person))

# Accessing Dictionary Items
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
print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
# print(person['city'])       # Error


## Adding Items to a Dictionary

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
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)

## Modifying Items in a Dictionary

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
person['first_name'] = 'Eyob'
person['age'] = 252
print(person)

## Checking Keys in a Dictionary

# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False

## Removing Key and Value Pairs from a Dictionary

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_married']        # Removes the is_married item

print(person)

## Changing Dictionary to a List of Items
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])

## Clearing a Dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None

## Deleting a Dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct

## Copy a Dictionary
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

## Getting Dictionary Values as a List
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])


#############################################
############# Exercises ####################
###########################################

#1 Create an empty dictionary called dog
dog = {}
print(dog)

#2 Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'lu'
dog['color'] = 'black'
dog['breed'] = 'co'
dog['legs'] = '4'
dog['age'] = '2'

print(dog)

#3 Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
# Create an empty dictionary to store student information
student = {}

student['first_name'] = 'John'
student['last_name'] = 'Doe'
student['gender'] = 'Male'
student['age'] = 20
student['marital_status'] = 'Single'
student['skills'] = ['Python', 'Java', 'C++']
student['country'] = 'USA'
student['city'] = 'New York'
student['address'] = '123 Main Street'

print(student)

#4 Get the length of the student dictionary
print(len(student))

#5 Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))

#6 Modify the skills values by adding one or two skills
student['skills'].append('HTML')
print(student)

#7 Get the dictionary keys as a list
print(student.keys())

#8 Get the dictionary values as a list
print(student.values())

#9 Change the dictionary to a list of tuples using items() method
print(student.items())

#10 Delete one of the items in the dictionary
student.pop('first_name')
student.popitem()
print(student)

#11 Delete one of the dictionaries
# del student
# print(student)













