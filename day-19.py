##########################################
############# File Handling #############
########################################

## open files
# # Syntax
# open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update

    # "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
    # "a" - Append - Opens a file for appending, creates the file if it does not exist
    # "w" - Write - Opens a file for writing, creates the file if it does not exist
    # "x" - Create - Creates the specified file, returns an error if the file exists
    # "t" - Text - Default value. Text mode
    # "b" - Binary - Binary mode (e.g. images)

# ## Opening Files for Reading
# f = open('./files/reading_file_example.txt')
# print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>

# # read(): read the whole text as string

# f = open('./files/reading_file_example.txt')
# txt = f.read()
# print(type(txt))
# print(txt)
# f.close()


# # readline(): read only the first line
# f = open('./files/reading_file_example.txt')
# line = f.readline()
# print(type(line))
# print(line)
# f.close()

# # readlines(): read all the text line by line and returns a list of lines
# f = open('./files/reading_file_example.txt')
# lines = f.readlines()
# print(type(lines))
# print(lines)
# f.close()

# # Another way to get all the lines as a list is using splitlines():
# f = open('./files/reading_file_example.txt')
# lines = f.read().splitlines()
# print(type(lines))
# print(lines)
# f.close()


# ## open and close it by itself with with:
# with open('./files/reading_file_example.txt') as f:
#     lines = f.read().splitlines()
#     print(type(lines))
#     print(lines)


## Opening Files for Writing and Updating
# example

# with open('./files/reading_file_example.txt','a') as f:
#     f.write('This text has to be appended at the end')

# The method below creates a new file, if the file does not exist:

with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')

## Deleting Files
# using os

import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')

## File Types
# File with txt Extension
 # File with txt extension is a very common form of data

# File with json Extension/ JSON : JavaScript Object Notation/ kí hiệu đối tượng JS
# Example
# dictionary
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''


#$#@$@ Changing JSON to Dictionary
import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])


#!$#!@#!@ Changing Dictionary to JSON
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)


#$#@$@ Saving as JSON File
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)


# %@#%# File with csv Extension
    # Example:
        # "name","country","city","skills"
        # "Asabeneh","Finland","Helsinki","JavaScript"

import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')

# &^%&# File with xlsx Extension
    # To read excel files we need to install xlrd package. We will cover this after we cover package installing using pip.

# import xlrd
# excel_book = xlrd.open_workbook('./files/sample.xlsx')
# print(excel_book.nsheets)
# print(excel_book.sheet_names)

#*^&%*&^  File with xml Extension
    # For more information on how to read an XML file check the documentation https://docs.python.org/2/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)



###############################################
############# Exercises: Level 1 #############
#############################################

#1 Write a function which count number of lines and number of words in a text. All the files are in the data the folder: 
    # a) Read obama_speech.txt file and count number of lines and words 
    # b) Read michelle_obama_speech.txt file and count number of lines and words 
    # c) Read donald_speech.txt file and count number of lines and words 
    # d) Read melina_trump_speech.txt file and count number of lines and words
    
import re

def number_of_lines_and_words(file_name_dir = ''):
    with open(file_name_dir, 'r') as f:
        lines = f.read().splitlines()
        remove_empty_lines = [line for line in lines if line.strip()]       # strip check if line đó có empty hay không
        number_of_lines = len(remove_empty_lines)
    
    with open(file_name_dir, 'r') as f:
        words = f.read()
        find_all_words = re.findall('[A-Za-z0-9]+', words)
        count_words = len(find_all_words)
    
    return f'number of lines in {file_name_dir} is {number_of_lines} lines\nnumber of words in {file_name_dir} is {count_words} words'
        
        
print(number_of_lines_and_words('./data/obama_speech.txt'))
print(number_of_lines_and_words('./data/michelle_obama_speech.txt'))
print(number_of_lines_and_words('./data/donald_speech.txt'))
print(number_of_lines_and_words('./data/melina_trump_speech.txt'))




#2 Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

    # # Your output should look like this
    # print(most_spoken_languages(filename='./data/countries_data.json', 10))
    # [(91, 'English'),
    # (45, 'French'),
    # (25, 'Arabic'),
    # (24, 'Spanish'),
    # (9, 'Russian'),
    # (9, 'Portuguese'),
    # (8, 'Dutch'),
    # (7, 'German'),
    # (5, 'Chinese'),
    # (4, 'Swahili'),
    # (4, 'Serbian')]

    # # Your output should look like this
    # print(most_spoken_languages(filename='./data/countries_data.json', 3))
    # [(91, 'English'),
    # (45, 'French'),
    # (25, 'Arabic')]
import json

def most_spoken_languages(file_name='./data/countries_data.json', top=10):
    with open(file_name, 'r', encoding='utf-8') as f:
        read_f = json.load(f)

    lg_list_all = []
    for index in range(len(read_f)):
        lg_list_all = lg_list_all + read_f[index]['languages']
        
    count_languages = []
    for language in set(lg_list_all):
        count = lg_list_all.count(language)
        count_languages.append((count, language))

    count_languages.sort(reverse=True)

    return count_languages[0:top]

print(most_spoken_languages(file_name='./data/countries_data.json', top=3))



#3 Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

    # Your output should look like this
    # print(most_populated_countries(filename='./data/countries_data.json', 10))

    # [
    # {'country': 'China', 'population': 1377422166},
    # {'country': 'India', 'population': 1295210000},
    # {'country': 'United States of America', 'population': 323947000},
    # {'country': 'Indonesia', 'population': 258705000},
    # {'country': 'Brazil', 'population': 206135893},
    # {'country': 'Pakistan', 'population': 194125062},
    # {'country': 'Nigeria', 'population': 186988000},
    # {'country': 'Bangladesh', 'population': 161006790},
    # {'country': 'Russian Federation', 'population': 146599183},
    # {'country': 'Japan', 'population': 126960000}
    # ]

    # # Your output should look like this

    # print(most_populated_countries(filename='./data/countries_data.json', 3))
    # [
    # {'country': 'China', 'population': 1377422166},
    # {'country': 'India', 'population': 1295210000},
    # {'country': 'United States of America', 'population': 323947000}
    # ]

import json

def most_populated_countries(file_name='./data/countries_data.json', top=10):
    with open(file_name, 'r', encoding='utf-8') as f:
        read_f = json.load(f)

    sort_data = sorted(read_f, key=lambda x: x['population'], reverse=True)

    hading_data = []

    for i in range(len(sort_data)):
        country = sort_data[i]['name']
        population = sort_data[i]['population']
        hading_data.append({'country': country, 'population': population})

    return hading_data[0:top]
    

print(most_populated_countries(file_name='./data/countries_data.json', top=3))



###############################################
############# Exercises: Level 2 #############
#############################################

#4 Extract all incoming email addresses as a list from the email_exchange_big.txt file.

with open('./data/email_exchanges_big.txt', 'r') as f:
    text_email = f.read()

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' # quan trọng

email_addresses = re.findall(pattern, text_email)

print(len(email_addresses))
    
#5 Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output

    # Your output should look like this
    # print(find_most_common_words('sample.txt', 10))
    # [(10, 'the'),
    # (8, 'be'),
    # (6, 'to'),
    # (6, 'of'),
    # (5, 'and'),
    # (4, 'a'),
    # (4, 'in'),
    # (3, 'that'),
    # (2, 'have'),
    # (2, 'I')]
    # # Your output should look like this
    # print(find_most_common_words('sample.txt', 5))
    # [(10, 'the'),
    # (8, 'be'),
    # (6, 'to'),
    # (6, 'of'),
    # (5, 'and')]

def find_most_common_words(text, top):
    if text.endswith('.txt'):
        with open(text, 'r') as f:
            text = f.read()
    else:
        pass

    num = re.findall('[A-Za-z]+', text)
    return_result = []
    for i in set(num):
        count = num.count(i)
        return_result.append((count, i))

    return_result.sort(reverse=True)

    return return_result[0:top]

print(find_most_common_words('Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelles and Melinas speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory', 3))


#6 Use the function, find_most_frequent_words to find: 
    #a) The ten most frequent words used in Obama's speech 
    #b) The ten most frequent words used in Michelle's speech 
    #c) The ten most frequent words used in Trump's speech 
    #d) The ten most frequent words used in Melina's speech

print(find_most_common_words('./data/obama_speech.txt', 10))
print(find_most_common_words('./data/michelle_obama_speech.txt', 10))
print(find_most_common_words('./data/donald_speech.txt', 10))
print(find_most_common_words('./data/melina_trump_speech.txt', 10))

    
#7 Write a python application that checks similarity (sự giống nhau) between two texts. It takes a file or a string as a parameter and it will evaluate(đánh giá) the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory

### No hope

    
#8 Find the 10 most repeated words in the romeo_and_juliet.txt

print(find_most_common_words('./data/romeo_and_juliet.txt', 10))

#9 Read the hacker news csv file and find out: 
    #a) Count the number of lines containing python or Python 
    #b) Count the number lines containing JavaScript, javascript or Javascript 
    #c) Count the number lines containing Java and not JavaScript


import csv

with open('./data/hacker_news.csv', 'r') as f:
    read_f = csv.reader(f, delimiter=',')
    count_a = 0
    count_b = 0
    count_c = 0
    for row in read_f:
        join_string = ' '.join(row)
        if 'python' in join_string.lower():
            count_a = count_a + 1
        elif 'javascript' in join_string.lower():
            count_b = count_b + 1
        elif 'Java' in join_string and 'JavaScript' not in join_string:
            count_c = count_c + 1
        else:
            continue
    print(f'the number of lines containing python or Python is {count_a} line')
    print(f'tCount the number lines containing JavaScript, javascript or Javascript is {count_b} line')
    print(f'the number lines containing Java and not JavaScript is {count_c} line')
        










