#Beautiful Soup is a Python library for pulling data out of HTML and XML files. It creates a parse tree for parsed pages that can be used to extract data from HTML.
from bs4 import BeautifulSoup
import requests

with open ('sample.html') as html_file:
	soup= BeautifulSoup(html_file,'lxml')

print(soup.prettify()) #prettify is used to clean the text by printing along with indentation

match = soup.title
#print(match)
match1 =soup.find('div',class_="article") #finds the first 'div' in the html page
#print(match1)

headline=match1.h3.text
print(headline)

summary= match1.p.text
print(summary)

# for all the 'divs' with classname article 'for' loop is used to access
 #all of it together

for article in soup.find_all('div', class_="article"):
	headlinee=article.h3.text

	print(headlinee)

	summmary=article.p.text
	print(summmary)

	


