# -*- coding: utf-8 -*-
"""
Created on Thu Dec 01 10:44:19 2016

@author: alsherman
"""

'''
PART ONE
    learn how to read html with requests &
    scrape data with Beautiful Soup 
'''

# requests
import requests

url = r'https://raw.githubusercontent.com/Alexjmsherman/python_for_data_analysis/master/Data_Scraping_APIs_and_Automation/data/example_html.html'
r = requests.get(url)
r.status_code
r.text

# read html into Beautiful Soup
from bs4 import BeautifulSoup

b = BeautifulSoup(r.text)


# .find


# .text


# .attrs


# select attribute


# .find_all


# slice the results


# iterate over the results


'''
EXERCISE ONE
'''

# find the 'h2' tag and then print its text


# find the 'p' tag with an 'id' value of 'reproducibility' 
# and then print its text


# find the first 'p' tag and then print the value of the 'id' attribute


# print the text of all four li tags


# bonus question: print the text of only the API resources



'''
PART TWO
    analyze HTML from opm.gov
'''

# view the robots.txt
# https://www.opm.gov/robots.txt

# HTML from opm.gov
url = r'https://www.opm.gov/'
r = requests.get(url)
b = BeautifulSoup(r.text)

# find the first blog post


# get the blog Title


# get the date the blog was posted


# get the blog text



'''
EXERCISE 2
'''

# HTML from opm.gov/data
url = r'https://www.opm.gov/data/Index.aspx?tag=FedScope'
r = requests.get(url)
b = BeautifulSoup(r.text)

# find the html for the table of files (HINT: look for the class DataTable)
data_table = 

# find the html for the first row of files (HINT: make sure to skip the table headers)
data_row = 

# find the 'td' element with the .zip link (HINT: look for 'a href')
url = 

# get the zip url



'''
PART THREE
    -Use selenium for web browser automation
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# specify which browser to use (Chrome)
# https://chromedriver.storage.googleapis.com/index.html?path=2.25/
browser = webdriver.Chrome(r'chromedriver\chromedriver.exe')
browser.implicitly_wait(2)

# open a browser
browser.get(r'https://www.opm.gov/data/Index.aspx?tag=FedScope')

# select an item in the sort by box
browser.find_element_by_xpath(
    r'//*[@id="ctl01_ctl00_MainContentPlaceHolder_MainContentPlaceHolder_SortCol"]/option[2]'
    ).click()

### Press 'go' button


# type and submit a query in the search box
inputbox = browser.find_element_by_xpath()
inputbox.send_keys('Type a query here')
inputbox.send_keys(Keys.ENTER)

# select the assessment drop down


# get_first_zip_link
html = browser.find_element_by_xpath()
link = html.get_attribute('href')

# close the browser


# download and open the zip file
#from download_zip import download_zip_file
data = download_zip_file(link, pandas=True)
data.open_zip()


'''
PART FOUR
    -APIs
'''

# XML
xml_url = r'https://raw.githubusercontent.com/Alexjmsherman/python_for_data_analysis/master/Data_Scraping_APIs_and_Automation/data/example_xml.xml'
r = requests.get(xml_url)
b = BeautifulSoup(r.text, 'xml')

# find the fourth topic


# collect data from google maps api
# documentation: https://developers.google.com/maps/documentation/geocoding/start
address = 'TYPE AN ADDRESS HERE'
api_url = r'https://maps.googleapis.com/maps/api/geocode/xml?address={}'.format(address)
r = requests.get(api_url)
b = BeautifulSoup(r.text, 'xml')

# find the status code


# find the postal code


# find the latitude and longitude


# use a python api wrapper package for google maps
# https://github.com/googlemaps/google-maps-services-python
import googlemaps  

# instantiate an api object
gmaps = googlemaps.Client(key='INSERT YOUR API KEY HERE')

# call a method on the api
gmaps.reverse_geocode((latitude,longitude))

# find nearby places of interest
place = 'TYPE A PLACE'
gmaps.places(place, location=(latitude, longitude), radius=1000)


# json
import json

# The missing JSON inspector for chrome 
# https://chrome.google.com/webstore/detail/the-missing-json-inspecto/hhffklcokfpbcajebmnpijpkaeadlgfn
address = 'TYPE AN ADDRESS HERE'
api_json_url = r'https://maps.googleapis.com/maps/api/geocode/json?address={}'.format(address)
r = requests.get(api_json_url)

# get the latitude and longitude from json
