################################################
############# Classes and Objects #############
##############################################


# Classes and Objects

### Creating a Class

# Example:

# class Person:
#   pass
# print(Person)


### Creating an Object

# p = Person()
# print(p)


#&*^@%  "object được tạo ra từ class"


## Class Constructor
# In the examples above, we have created an object from the Person class. However, a class without a constructor is not really useful in real applications. Let us use constructor function to make our class more useful. Like the constructor function in Java or JavaScript, Python has also a built-in init() constructor function. The init constructor function has self parameter which is a reference to the current instance of the class

class Person:
      def __init__ (self, name):
        # self allows to attach parameter to the class
          self.name = name

p = Person('Asabeneh')
print(p.name)
print(p)


###!@@#s@!

class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city


p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)



##!@#@! Object Methods

# Objects can have methods. The methods are functions which belong to the object.

# Example 
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())


##!#$!@ Object Default Methods
# Sometimes, you may want to have a default values for your object methods. If we give default values for the parameters in the constructor, we can avoid errors when we call or instantiate our class without parameters. Let's see how it looks:

class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())


## !@$#!@ Method to Modify Class Default Values
# In the example below, the person class, all the constructor parameters have default values. In addition to that, we have skills parameter, which we can access using a method. Let us create add_skill method to add skills to the skills list.

class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)


##!#@!3 Inheritance / kế thừa/ di sản
# Using inheritance we can reuse parent class code. Inheritance allows us to define a class that inherits all the methods and properties from parent class. The parent class or super or base class is the class which gives all the methods and properties. Child class is the class that inherits from another or parent class. Let us create a student class by inheriting from person class.

class Student(Person):
    pass


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)


###!@!@# Overriding parent method
# We did not call the init() constructor in the child class. If we didn't call it then we can still access all the properties from the parent. But if we do call the constructor we can access the parent properties by calling 'super'.
# We can add a new method to the child or we can override the parent class methods by creating the same method name in the child class. When we add the init() function, the child class will no longer inherit the parent's init() function.

class Student(Person):
    def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)


##############################################
############# Exercises: Level 1 ############
############################################

#1. Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.

    # ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

    # print('Count:', data.count()) # 25
    # print('Sum: ', data.sum()) # 744
    # print('Min: ', data.min()) # 24
    # print('Max: ', data.max()) # 38
    # print('Range: ', data.range() # 14
    # print('Mean: ', data.mean()) # 30 / trung binh
    # print('Median: ', data.median()) # 29 / trung vi
    # print('Mode: ', data.mode()) # {'mode': 26, 'count': 5} / xuat hien nhieu nhat
    # print('Standard Deviation: ', data.std()) # 4.2   /độ lệch chuẩn  / căn bậc 2 trung bình cộng của (Xi - Xmean) bình phương
    # print('Variance: ', data.var()) # 17.5    / độ lệch chuẩn bình phương
    # print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)] / (tính phần trăm số lần xuất hiện)

class Statistics:
    def __init__ (self, age=[]) -> None:
        self.age = age
    def count(self):
        return len(self.age)
    def sum(self):
        sum_all = 0
        for i in self.age:
            sum_all = sum_all + i
        return sum_all
    def min(self):
        min_age = self.age[0]
        for i in range(len(self.age) - 1):
            if self.age[i+1] < min_age:
                min_age = self.age[i+1]
            else:
                continue
        return min_age
    def max(self):
        max_age = self.age[0]
        for i in range(len(self.age) - 1):
            if self.age[i+1] > max_age:
                max_age = self.age[i+1]
            else:
                continue
        return max_age
    def range(self):
        range_age = Statistics.max(self) - Statistics.min(self)
        return range_age
    def mean(self):
        ave = Statistics.sum(self)/Statistics.count(self)
        return round(ave) # round làm tròn lên
    def median(self):
        list_age = self.age
        list_age.sort()
        return list_age[len(list_age)//2] # // làm tròn xuống
    def mode(self):
        mode_count = []
        get_list = self.age
        for i in set(get_list):
            count = get_list.count(i)
            mode_count.append({'mode': i, 'count': count})
        mode_count = sorted(mode_count, key=lambda x: x['count'], reverse=True)
        return mode_count[0]
    


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print('Count:', data.count())
print('Sum: ', data.sum())
print('Min: ', data.min())
print('Max: ', data.max())
print('Range: ', data.range())
print('Mean: ', data.mean())
print('Median: ', data.median())
print('Mode: ', data.mode())


##############################################
############# Exercises: Level 2 ############
############################################


#1. Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.
class PersonAccount:
  """
  This class represents a person's account with income, expenses, and balance.
  """

  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name
    self.incomes = set()  # Set to store unique income descriptions and amounts
    self.expenses = set()  # Set to store unique expense descriptions and amounts

  def total_income(self):
    """
    Calculates the total income by summing all income amounts.
    """
    total = 0
    for income in self.incomes:
      total += income[1]  # Access income amount from the tuple
    return total

  def total_expense(self):
    """
    Calculates the total expense by summing all expense amounts.
    """
    total = 0
    for expense in self.expenses:
      total += expense[1]  # Access expense amount from the tuple
    return total

  def account_info(self):
    """
    Provides a string representation of the account information.
    """
    return f"Account Holder: {self.first_name} {self.last_name}\nTotal Income: ${self.total_income()}\nTotal Expense: ${self.total_expense()}"

  def add_income(self, description, amount):
    """
    Adds a new income description and amount to the incomes set.
    """
    self.incomes.add((description, amount))

  def add_expense(self, description, amount):
    """
    Adds a new expense description and amount to the expenses set.
    """
    self.expenses.add((description, amount))

  def account_balance(self):
    """
    Calculates the account balance by subtracting total expenses from total income.
    """
    return self.total_income() - self.total_expense()


# Example usage
account = PersonAccount("John", "Doe")
account.add_income("Salary", 2000)
account.add_income("Investment return", 100)
account.add_expense("Rent", 1200)
account.add_expense("Groceries", 500)

print(account.account_info())
print(f"Account Balance: ${account.account_balance()}")
