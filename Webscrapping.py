from bs4 import BeautifulSoup
import requests

urlh = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(urlh)
soup = BeautifulSoup(page.text, 'html.parser')

print(soup)

soup.find ('table', class_='wikitable sortable')
#<table class="wikitable sortable jquery-tablesorter">
#<caption>

table = soup.find_all('table')[1]
print(table)


world_titles = soup.find_all('th')