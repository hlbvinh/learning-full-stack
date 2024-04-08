#########################################
############# Web Scraping #############
#######################################

### Python Web Scraping

# What is Web Scrapping
"""
The internet is full of huge amount of data which can be used for different purposes. To collect this data we need to know how to scrape data from a website.
Web scraping is the process of extracting and collecting data from websites and storing it on a local machine or in a database.
In this section, we will use beautifulsoup and requests package to scrape data. The package version we are using is beautifulsoup 4.
To start scraping websites you need requests, beautifoulSoup4 and a website.
"""

import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/dataset/53/iris'

# Lets use the requests get method to fetch the data from url

response = requests.get(url)
# lets check the status
status = response.status_code
print(status) # 200 means the fetching was successful

#######################################################################
## Using beautifulSoup to parse content from the page

response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
#print(soup.body) # gives the whole page on the website
print(response.status_code)

tables = soup.find_all('table', {'class':'my-4 table w-full'})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0] # the result is a list, we are taking out data from it
for td in table.find('tr').find_all('td'):
    print(td.text)



##############################################
############# Exercises: Day 22 #############
############################################


#1 Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
import requests
from bs4 import BeautifulSoup
import json

def scrape_website(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Tìm tất cả các phần tử <ul>
        all_ul = soup.find_all('ul')
        
        data = {}
        for index, ul in enumerate(all_ul, start=1): # lặp qua tất cả các phần tử trong danh sách all_ul và cung cấp cả vị trí của mỗi phần tử trong danh sách.
            # Tìm tất cả các phần tử <li> trong mỗi <ul>
            list_items = ul.find_all('li')
            ul_data = {}
            for item_index, item in enumerate(list_items, start=1):
                # Trích xuất nội dung của mỗi phần tử <li> và lưu vào từ điển
                ul_data[f"item_{item_index}"] = item.get_text(strip=True)
            # Lưu từ điển của mỗi <ul> vào trong dữ liệu chính
            data[f"ul_{index}"] = ul_data
        
        return data
    else:
        print("Failed to fetch the webpage.")
        return None

url = 'http://www.bu.edu/president/boston-university-facts-stats/'
data = scrape_website(url)

if data:
    with open('bu_facts.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("Data saved successfully as 'bu_facts.json'")
else:
    print("No data to save.")




#2 Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file
import requests
from bs4 import BeautifulSoup
import json

url = 'https://en.wikipedia.org/wiki/AFI%27s_100_Years...100_Movies#:~:text=%20%20%20%20Film%20%20%20,%20%204%20%2025%20more%20rows%20'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
tables = soup.find_all('table')
data = {}
for table in tables:
    for td in table.find('tr').find_all('td'):
        print(td.text)







#3 Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.


# do this exercise later




















