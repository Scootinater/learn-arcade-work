'''
Example showing how to read in from a web page
'''

from bs4 import BeautifulSoup
import urllib.request

# read in the web page
url_address = 'http://mandaria.net'
page = urllib.request.urlopen(url_address)

# parse the web page
soup = BeautifulSoup(page.read(), 'html.parser')

# get a list of level 1 headings in the page
headings = soup.findAll('h1')

# loop through each row
for heading in headings:
    print(heading.text)
