################################################################
############# Python PIP - Python Package Manager #############
##############################################################


# pip install numpy

import numpy

# asabeneh@Asabeneh:~$ python
# Python 3.9.6 (default, Jun 28 2021, 15:26:21)
# [Clang 11.0.0 (clang-1100.0.33.8)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import numpy
# >>> numpy.version.version
# '1.20.1'
# >>> lst = [1, 2, 3,4, 5]
# >>> np_arr = numpy.array(lst)
# >>> np_arr
# array([1, 2, 3, 4, 5])
# >>> len(np_arr)
# 5
# >>> np_arr * 2
# array([ 2,  4,  6,  8, 10])
# >>> np_arr  + 2
# array([3, 4, 5, 6, 7])
# >>>



#&^$ pip install pandas


# import webbrowser # web browser module to open websites

# # list of urls: python
# url_lists = [
#     'http://www.python.org',
#     'https://www.linkedin.com/in/asabeneh/',
#     'https://github.com/Asabeneh',
#     'https://twitter.com/Asabeneh',
# ]

# # opens the above list of websites in a different tab
# for url in url_lists:
#     webbrowser.open_new_tab(url)


#*#&s3 pip uninstall packagename


## **@&^@!#^ PIP Freeze / in ra all version pip package in-use


### Reading from URL
    
# By now you are familiar with how to read or write on a file located on you local machine. Sometimes, we would like to read from a website using url or from an API. API stands for Application Program Interface. It is a means to exchange structured data between servers primarily as json data. To open a network connection, we need a package called requests - it allows to open a network connection and to implement CRUD(create, read, update and delete) operations. In this section, we will cover only reading ore getting part of a CRUD.    

#@!^#!*# pip install requests

# We will see get, status_code, headers, text and json methods in requests module:

# get(): to open a network and fetch data from url - it returns a response object
# status_code: After we fetched data, we can check the status of the operation (success, error, etc)
# headers: To check the header types
# text: to extract the text from the fetched response object
# json: to extract json data Let's read a txt file from this website, https://www.w3.org/TR/PNG/iso_8859-1.txt.



# import requests # importing the request module

# url = 'https://www.w3schools.com/' # text from a website

# response = requests.get(url) # opening a network and fetching a data
# print(response)
# print(response.status_code) # status code, success:200
# print(response.headers)     # headers information
# print(response.text) # gives all the text from the page



# import requests
# url = 'https://restcountries.com/v3.1/all'  # countries api
# response = requests.get(url)  # opening a network and fetching a data
# print(response) # response object
# print(response.status_code)  # status code, success:200
# countries = response.json()
# print(countries[:1])  # we sliced only the first country, remove the slicing to see all countries



#*&#@ Creating a Package

# We organize a large number of files in different folders and sub-folders based on some criteria, so that we can find and manage them easily. As you know, a module can contain multiple objects, such as classes, functions, etc. A package can contain one or more relevant modules. A package is actually a folder containing one or more module files. Let us create a package named mypackage, using the following steps:
# Create a new folder named mypacakge inside 30DaysOfPython folder Create an empty init.py file in the mypackage folder. Create modules arithmetic.py and greet.py



## *&^@*&^*@ Further Information About Packages

#1 Database
    # SQLAlchemy or SQLObject - Object oriented access to several different database systems
        # pip install SQLAlchemy

#2 Web Development
    # Django - High-level web framework.
        # pip install django
    # Flask - micro framework for Python based on Werkzeug, Jinja 2. (It's BSD licensed)
        # pip install flask

#3 HTML Parser
    # Beautiful Soup - HTML/XML parser designed for quick turnaround projects like screen-scraping, will accept bad markup.
        # pip install beautifulsoup4
    # PyQuery - implements jQuery in Python; faster than BeautifulSoup, apparently.

#4 XML Processing
    # ElementTree - The Element type is a simple but flexible container object, designed to store hierarchical data structures, such as simplified XML infosets, in memory. --Note: Python 2.5 and up has ElementTree in the Standard Library

#5 GUI
    # PyQt - Bindings for the cross-platform Qt framework.
    # TkInter - The traditional Python user interface toolkit.

#6 Data Analysis, Data Science and Machine learning
    # Numpy: Numpy(numeric python) is known as one of the most popular machine learning library in Python.
    # Pandas: is a data analysis, data science and a machine learning library in Python that provides data structures of high-level and a wide variety of tools for analysis.
    # SciPy: SciPy is a machine learning library for application developers and engineers. SciPy library contains modules for optimization, linear algebra, integration, image processing, and statistics.
    # Scikit-Learn: It is NumPy and SciPy. It is considered as one of the best libraries for working with complex data.
    # TensorFlow: is a machine learning library built by Google.
    # Keras: is considered as one of the coolest machine learning libraries in Python. It provides an easier mechanism to express neural networks. Keras also provides some of the best utilities for compiling models, processing data-sets, visualization of graphs, and much more.

#7 Network:
    # requests: is a package which we can use to send requests to a server(GET, POST, DELETE, PUT)
        # pip install requests





##############################################
############# Exercises: Day 20 #############
############################################

#1 Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
# import requests
# url = "https://www.gutenberg.org/help/file_formats.html#txt"

# get = requests.get(url)
# print(get.text)



#2 Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
    #i the min, max, mean, median, standard deviation of cats' weight in metric units.
    #ii the min, max, mean, median, standard deviation of cats' lifespan in years.
    #iii Create a frequency table of country and breed of cats

import requests
import numpy as np
import pandas as pd

# Fetch data from the API
cats_api = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(cats_api)
data = response.json()


# Extract weights and lifespans
weights = [cat['weight']['metric'].split()[0] for cat in data if 'weight' in cat]
lifespans = [cat['life_span'] for cat in data if 'life_span' in cat]

# Convert weights to numeric
weights = [float(w) for w in weights if w != 'unknown']

# Convert lifespans to numeric
lifespans = [float(ls.split()[0]) for ls in lifespans if ls != 'unknown']

# Calculate statistics
weight_stats = {
    'min': np.min(weights),
    'max': np.max(weights),
    'mean': np.mean(weights),
    'median': np.median(weights),
    'std': np.std(weights)
}

lifespan_stats = {
    'min': np.min(lifespans),
    'max': np.max(lifespans),
    'mean': np.mean(lifespans),
    'median': np.median(lifespans),
    'std': np.std(lifespans)
}

# Create a frequency table of country and breed of cats
country_breed_freq = pd.DataFrame({
    'country': [cat.get('origin', 'Unknown') for cat in data],
    'breed': [cat['name'] for cat in data]
}).groupby(['country', 'breed']).size().reset_index(name='frequency')

print("Statistics of Cat Weights (in metric units):")
print(weight_stats)
print("\nStatistics of Cat Lifespans (in years):")
print(lifespan_stats)
print("\nFrequency Table of Country and Breed of Cats:")
print(country_breed_freq.to_string(index=True))



#3 Read the countries API and find
    #i the 10 largest countries
    #ii the 10 most spoken languages
    #iii the total number of languages in the countries API

import requests

# Function to fetch data from the API
def fetch_data(url):
    response = requests.get(url)
    data = response.json()
    return data

# Fetch data from the countries API
countries_data = fetch_data("https://restcountries.com/v3.1/all")


# Function to get the 10 largest countries
def get_largest_countries(data):
    countries = sorted(data, key=lambda x: x['area'], reverse=True)[:10]
    return countries

# Function to get the 10 most spoken languages
def get_most_spoken_languages(data):
    languages = {}
    for country in data:
        for language in country.get('languages', []):
            languages[language] = languages.get(language, 0) + 1
    most_spoken = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:10] ## lambda x: x[1], có nghĩa là sắp xếp dựa trên phần tử thứ hai của mỗi tuple,
    return most_spoken

# Function to get the total number of languages
def get_total_languages(data):
    all_languages = set()
    for country in data:
        all_languages.update(country.get('languages', []))
    return len(all_languages)

# Get the results
largest_countries = get_largest_countries(countries_data)
most_spoken_languages = get_most_spoken_languages(countries_data)
total_languages = get_total_languages(countries_data)

# Print the results
print("10 Largest Countries:")
for country in largest_countries:
    print(country['name']['common'])

print("\n10 Most Spoken Languages:")
for language, count in most_spoken_languages:
    print(f"{language}: {count}")

print("\nTotal Number of Languages:", total_languages)





#4 UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4


from bs4 import BeautifulSoup

# URL of the UCI datasets page
url = "https://archive.ics.uci.edu/ml/datasets.php"

# Fetch the HTML content of the webpage
response = requests.get(url)
html_content = response.text

# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Find all links to datasets
dataset_links = soup.find_all("a")
print(dataset_links)

# Extract dataset names
dataset_names = [link.text.strip() for link in dataset_links]
print(dataset_names)

# Filter out empty strings and non-dataset links
dataset_names = [name for name in dataset_names if name]
print(dataset_names)

# Print the dataset names
for name in dataset_names:
    print(name)






















