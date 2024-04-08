#operator
x = 1
x &= 3 # AND lấy phần chung của x và 3 trong hệ nhị phân.
x |= 3 # OR lấy bit 1 trong hệ nhị phân
x ^= 3 # XOR trong hệ nhị phân
x >>= 3 # dịch phải x đi 3 bit.
x <<= 3 # dịch trái x đi 3 bit.


# interger
print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 9 it means 2 * 2 * 2

# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)


# Complex numbers : số phức 
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))


# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
print(total) # if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)


print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)


print("##############################################")

# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity # trọng lượng của một vật bằng khối lượng Mass nhân với gia tốc trọng trường  gravity
print(weight, 'N')                         # Adding unit to the weight

# Calculate the density of a liquid
mass = 75 # in Kg 
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3   # công thức tính khối lượng riêng của một vật 
print(density, 'Kg/m3')



#Comparison Operators
print("#####################################")
print("Comparison Operators")

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)

print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

#Logical Operators

print(not(1 < 3 or 1 > 2))
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False



#exercise 
print("######################################################################")
print("excercise")
print("######################################################################")

your_age = 18 # years old
your_hight = 169.5 # citimeter
so_phuc = 4 + 6j

b = float(input("enter base: "))
h = float(input("enter height: "))
print("The area of the triangle 0.5*b*h is: ", 0.5 *h *b )


print("nhap chieu dai 3 canh cua tam giac")
canh_a =  int(input("chieu dai canh a: "))
canh_b =  int(input("chieu dai canh b: "))
canh_c =  int(input("chieu dai canh c: "))
print("chu vi cua tam giac a + b + c bang: ", canh_a + canh_b + canh_c)


print("nhap chieu dai và chieu rong cua hinh chu nhat")
dai = float(input("nhap chieu dai: "))
rong = float(input("nhap chieu rong: "))
print("dien tich hinh chu nhat bang ", dai*rong)
print("chu vi hinh chu nhat bang ", 2*(dai+rong))


print("hinh tron")
radius = float(input("nhap ban kinh hinh tron: "))
pi = 3.14
print("dien tich hinh tron bang: ", pi*radius*radius)
print("chu vi hinh tron bang: ", 2*pi*radius)


#Calculate the slope, x-intercept and y-intercept of y = 2x -2\
# slope = hệ số của x =2
# x-intercept là giá trị của x khi y = 0 => x=1
# y-intercept là giá trị của y khi x = 0 => y=-2

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10) 
# tính được slope m=2


print("Use and operator to check if 'on' is found in both 'python' and 'dragon'")
print('on' in ("python" and "dragon"))

print("I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.")
print("jargon" in "I hope this course is not full of jargon")



print("Find the length of the text python and convert the value to float and convert it to string")
text = "python"
lg_text = len(text)
print(type(float(lg_text)))
print(type(str(float(lg_text))))
print(type(str(lg_text)))

print(int(9.8) == 10)

# Check if the value of '10' is equal to the value of 10 after conversion
value_check = int('10') == 10

print("Is the value of '10' equal to the value of 10?", value_check)


print("Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?")
hours = int(input("nhap so gio su dung: "))
gia_1_gio = int(input("nhap gia 1 gio: "))

print("tong bill cua ban la: ", hours*gia_1_gio)


print("Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years")

years_of_lived = int(input("Enter number of years you have lived: "))

print("tong so giay ban da song la: ", years_of_lived*365*24*60*60, "seconds")

##Write a Python script that displays the following table
print("Write a Python script that displays the following table")
# Define the number of rows and columns in the table
num_rows = 5
num_cols = 5

# Loop over each row
for i in range(1, num_rows + 1):
    # Print the current row
    for j in range(1, num_cols + 1):
        # Calculate the value based on the pattern
        if j == 1:
            value = i
        elif j == 2:
            value = 1
        else:
            value = i ** (j - 2)
        # Print the value with a space separator
        print(value, end=' ')
    # Move to the next line after printing each row
    print()


# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
