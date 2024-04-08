#################$##############################
############## SET #########################
#################$#########################

#  In Python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.

## Creating a Set

# Creating an empty set
st = set()

# Creating a set with initial items
st = {'item1', 'item2', 'item3', 'item4'}

# Getting Set's Length
fruits = {'banana', 'orange', 'mango', 'lemon'}
len(fruits)

# Accessing Items in a Set
    ## We use loops to access items. We will see this in loop section

# Checking an Item
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True

# Adding Items to a SetS
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')


# Add multiple items using update() The update() allows to add multiple items to a set. The update() takes a list argument.
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot') # tuples s
fruits.update(vegetables)

# Removing Items from a Set
# We can remove an item from a set using remove() method. If the item is not found remove() method will raise errors, so it is good to check if the item exist in the given set. 
# However, discard() method doesn't raise any errors.
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')

# The pop() methods remove a random item from a list and it returns the removed item.
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set

# Clearing Items in a Set
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()

# Deleting a Set
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

# Converting List to Set
# We can convert list to set and set to list. Converting list to set removes duplicates and only unique items will be reserved.
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}


# Joining Sets
# using union()
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

# using update()
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

## Finding Intersection Items
# Intersection returns a set of items which are in both the sets. See the example/ lấy phần giao nhau (phần chung) của 2 set
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}

##Checking Subset and Super Set/ có thể hiểu là check xem set này có phải là tập hợp con (subset) hay là tập hợp cha (supper set) của tập hợp kia và ngược lại
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.issubset(dragon))     # False
print(python.issuperset(dragon)) # False as well

## Checking the Difference Between Two Sets / tìm ra phần tử trong set này có mà set kia không có 
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
dragon.difference(python)     # {'d', 'r', 'a', 'g'}

## Finding Symmetric Difference Between Two Sets / tim sự khác biệt đối xưng: / có nghĩa là bằng 2 difference của 2 thằng công lại
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}

##Joining Sets
# If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or disjoint using isdisjoint() method.
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}


#############################################
############# Exercises: Level 1 ###########
###########################################
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

#1 Find the length of the set it_companies
print(len(it_companies))

#2 Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#3 Insert multiple IT companies at once to the set it_companies
it_com_update = ('tma', 'acb', 'yui')
it_companies.update(it_com_update)
print(it_companies)

#4 Remove one of the companies from the set it_companies
it_companies.remove('tma')
print(it_companies)

#5 What is the difference between remove and discard
# remove() sẽ raise error nếu không tìm thấy item còn discard() thì không raise error



#############################################
############# Exercises: Level 2 ###########
###########################################
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
#1 Join A and B
print(A.union(B))

#2 Find A intersection B
print(A.intersection(B))

#3 Is A subset of B
print(A.issubset(B))

#4 Are A and B disjoint sets
print(A.isdisjoint(B))

#5 Join A with B and B with A
A.update(B)
B.update(A)
print("A after joining with B:", A)
print("B after joining with A:", B)

#6 What is the symmetric difference between A and B
print(A.symmetric_difference(B))

#7 Delete the sets completely
del A
del B

#############################################
############# Exercises: Level 3 ###########
###########################################
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1 Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(age_set)
len_age = len(age)
len_set = len(age_set)

print(len_age)
print(len_set)

#2 Explain the difference between the following data types: string, list, tuple and set
# string là 1 chuỗi bình thường nằm trong dâu "" or ''
# list là tập hợp danh sách binh thường, nằm trong dâu ngươc vuông [ ]
# tuple: tập hợp item k thể thêm xóa sửa sau khi tạo, nằm trong dấu ( )
# set: là tập hợp item khong có indexing và data là unique, nằm trong dấu { }

#3 I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
string1 = "I am a teacher and I love to inspire and teach people"
string1_new = string1.split(" ")
print(string1_new)
string1_set = set(string1_new)
print(string1_set)













st = set()
print(st)
lst = [1, 2, 3]

st.update(lst)
print(st)












