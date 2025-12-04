import requests
import re
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

URL = "https://untappd.com/v/briggs-taphouse/11145609"
results = requests.get(URL, headers=headers)

soup = BeautifulSoup(results.text, 'html.parser')

# print(soup.prettify())
a = soup.find_all("a")
things = soup.find_all('a', href=True, string = re.compile('Russian River Brewing Co')) #re compile searches for everything roughly containing the string
#maybe could also search by href

print(len(a))

print(len(things))
for thing in things:
    print(thing)
# print(soup)

