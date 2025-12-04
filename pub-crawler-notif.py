import requests
import re
from bs4 import BeautifulSoup
from functools import reduce

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
} #make website trust you

URL = "https://untappd.com/v/briggs-taphouse/11145609"
results = requests.get(URL, headers=headers)

soup = BeautifulSoup(results.text, 'html.parser')

# print(soup.prettify())
a = soup.find_all("a")
things = soup.find_all('a', href=True, string = re.compile('Russian River Brewing Co')) #re compile searches for everything roughly containing the string
#maybe could also search by href

beerdetails = soup.find_all("div", class_ = re.compile("beer details"))

print(len(a))
print(len(beerdetails))

print(len(things))
for thing in things:
    # print("PARENT---------------------------------------------------------------------------")
    parent = thing.parent.parent.parent
    parentsoup = BeautifulSoup(parent.text, 'html.parser')
    parent_as = parentsoup.find_all('a')
    string = str(parentsoup)
    # print(string)
    cleaned_string1 = ""
    allowed_chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890-,./!?()"

    split = string.split("\n")

    print("SPLIT----------------")

    for i in split:
        if i != "":
            # print(i)
            cleaned_string1 += i

    replaced = cleaned_string1.replace("  ", "/")

    for i in range (1,10):
        replaced = replaced.replace("//", "/")

    new_string = replaced

    print(new_string)

    new_split = new_string.split("/")

    for i in new_split:
        print(i)
    
    # for char in string:
    #     if char in allowed_chars:
    #         cleaned_string2 += char
    # print(cleaned_string2)
    # if "Russian River" in str(parentsoup):
    #     print("Russian River")
# print(soup)

# for i in beerdetails:
#     print("BEER DETAILS--------------------------------------------------------------------")
#     print(i.text)
