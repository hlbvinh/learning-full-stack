### string
letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)

##multiline
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

## noi chuoi
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Asabeneh Yetayeh
# Checking the length of a string using len() built-in function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 16


##Escape Sequences in Strings
print("how are you? \nI'm fine")# \n: new line
print("hom nay la thu may?\tthu7")# \t: Tab means(8 spaces)
print("\\")# \\: Back slash
# \': Single quote (')
# \": Double quote (")

####String formatting
# Strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# Strings  and numbers
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# "%.number of digits" - Floating point numbers with fixed precision
# Strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point
print(formated_string)

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"


### New Style String Formatting (str.format) ONLY PYTHON 3 VERSION

first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)


#### String Interpolation / f-Strings (Python 3.6+)
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

### Python Strings as Sequences of Characters
#Unpacking Characters
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

#Accessing Characters in Strings by Index
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o


#Slicing Python Strings / cắt chuỗi
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

## Reversing a String/ đảo ngược chuỗi
greeting = "hello, world"
print(greeting[::-1])

# Skipping Characters While Slicing
language = 'Python'
pto = language[0:6:3] # [start:stop:step] step ở đây là bước nhảy
print(pto) # Pto

######  String Methods  #######
#capitalize():
challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'

#count() đếm phần tử trong chuỗi
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 
print(challenge.count('th')) # 2`

# endswith(): Checks if a string ends with a specified ending
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

#expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

# find(): Returns the index of the FIRST occurrence of a substring, if not found returns -1

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0
print(challenge.find('j'))

# rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17

#index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError.

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
#print(challenge.index(sub_string, 9)) # error

#rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 8
#print(challenge.rindex(sub_string, 9)) # error

# isalnum(): Checks alphanumeric character / kiểm tra ký tự chữ và số
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False

# isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

# isdecimal(): Checks if all characters in a string are decimal (0-9)
# isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True
print(challenge)
# isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False

#isidentifier() kiểm tra chuỗi có phải tên biến hợp lệ hay không
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True
#islower(): Checks if all alphabet characters in the string are lowercase
# isupper(): Checks if all alphabet characters in the string are uppercase
# join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'


# strip(): Removes all given characters starting from the beginning and end of the string
challenge = "       jyhgagsjdakjsd akjsdhkashd kajshd kjahs            "
print(challenge.strip('shajk'))


# replace(): Replaces substring with a given string
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

# split(): Splits the string, using given string or space as a separator / tách chuỗi
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty. days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']


# title(): Returns a title cased string
challenge = 'thirty days of python ádasdasdasdasdasd'
print(challenge.title()) # Thirty Days Of Python

# swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON


# startswith(): Checks if String Starts with the Specified String
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('days')) # False


########################
###### EXERCISE ########
########################

#1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
st1 = 'Thirty'
st2 = 'Days'
st3 = 'Of'
st4 = 'Python'
space =  ' '

stt = st1 + space + st2 + space + st3 + space + st4

print(stt)

#2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
st1 = 'Coding'
st2 = 'For'
st3 = 'All'
space =  ' '

stt = st1 + space + st2 + space + st3

print(stt)

#3 Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

#4 Print the variable company using print().
print(company)

#5 Print the length of the company string using len() method and print().
print(len(company))

#6 Change all the characters to uppercase letters using upper() method.
#7 Change all the characters to lowercase letters using lower() method.
COMPANY = company.upper()
COMPANY = company.lower()

#8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#9 Cut(slice) out the first word of Coding For All string.
print(company[0:6])

#10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index('Coding'))
print(company.find('Coding'))

#11 Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'coding'))

#12 Change Python for Everyone to Python for All using the replace method or other methods.
string = "Python for Everyone"
print(string.replace('Everyone', 'All'))

#13 Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

#14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
text1 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(text1.split(','))

#15 What is the character at index 0 in the string Coding For All.
print(company[0])

#16 What is the last index of the string Coding For All.
print(company[-1])

#17 What character is at index 10 in "Coding For All" string.
print(company[10])

#18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
text  = 'pytHon For Everyone'
new_texts = text.split()
rs = ''.join(new_text[0].upper() for new_text in new_texts)
print(rs)

#19 Create an acronym or an abbreviation for the name 'Coding For All'.
text  = 'Coding For All'
new_texts = text.split()
rs = ''.join(new_text[0].upper() for new_text in new_texts)
print(rs)

#20 Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))

#21 Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))

#22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
text = "Coding For All People"
print(text.rfind('l'))


#23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 
#'You cannot end a sentence with because because because is a conjunction
text = "You cannot end a sentence with because because because is a conjunction"
print(text.find("because"))
print(text.index("because"))


#24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'\
print(text.rfind("because"))
print(text.rindex("because"))

#25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"

# Starting index (inclusive) at the first "because"
start_index = sentence.find("because ")  # Find the first occurrence

# Ending index (exclusive) at the character after the last "because"
end_index = start_index + len("because because because ")

# Slice the sentence to get the desired phrase
sliced_phrase = sentence[start_index:end_index]

print(sliced_phrase)


#26 Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
#same 25

#27 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

#28 Does 'Coding For All' start with a substring Coding?
print(company.startswith("Coding"))
#29 Does 'Coding For All' end with a substring coding?
print(company.endswith("All"))

#30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
test = "   Coding For All      "
print(test.strip())

# Which one of the following variables return True when we use the method isidentifier():30DaysOfPython thirty_days_of_python
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

#32 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
lib_text = ' '.join(lib)
print(lib_text)

#33 Use the new line escape sequence to separate the following sentences
# I am enjoying this challenge.
# I just wonder what is next.

print("I\nam\nenjoying\nthis\nchallenge.")

#34 Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
chuoi1 = "Name\tAge\tCountry\tCity"
chuoi2 = "Vinh\t250\tFinland\tHelsinki"

print(chuoi1.expandtabs(10))
print(chuoi2.expandtabs(10))

# 35 Use the string formatting method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a circle with radius {radius} is {area:.0f} meters square.')
print("The area of a circle with radius {} is {:.0f} meters square.".format(radius, area))
print("The area of a circle with radius %d is %.0f meters square." %(radius, area))

#36 Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
a = 8
b = 6
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b:.2f}')
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')
