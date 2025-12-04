import requests
import re
from bs4 import BeautifulSoup
from functools import reduce
from win10toast import ToastNotifier

class TapList:
    def __init__(self, name):
        self.name = name
        self.beer_list = []

    def addBeer(self, beer, brewery):
        self.beer_list.append([beer, brewery])
        #maybe add tap_num? looks like not all pubs have one
    
    def brewerySearch(self, brewery_name):

        beers_from_brewery = []

        for beer in self.beer_list:
            brewery = beer[1] #list is two long
            if brewery_name in brewery:
                beers_from_brewery.append(beer)
        
        return beers_from_brewery
    
notifier = ToastNotifier()

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

print(len(a))

menu_items = soup.find_all("li", class_ = re.compile("menu-item"))
print(len(menu_items))

briggs = TapList("briggs_taplist")

for item in menu_items:
    # print(type(item))
    label = item.find("img")
    # print(label['src'])

    # data_hrefs = [elem['data-href'] for elem in item.select("a")]
    # print(data_hrefs)

    beer_title = item.css.select_one('a[data-href=":"]')

    if beer_title: #make it not break for menut items that dont have a ":" data-href, like the wines
        beer_title_text = beer_title.text
    else:
        beer_title_text = "not found"

    beer_title_text_stripped = beer_title_text.strip().replace("  ", "/").strip("\n")

    while "//" in beer_title_text_stripped:
        beer_title_text_stripped = beer_title_text_stripped.replace("//", "/")

    if "/" in beer_title_text_stripped:
        beer_name = beer_title_text_stripped.split("/")[1]
    else:
        beer_name = beer_title_text_stripped

    # print(beer_name)

    brewery = item.css.select_one('a[data-href=":brewery"]')

    if brewery:
        brewery_text = brewery.text
    else:
        brewery_text = "not found"

    brewery_text_stripped = brewery_text.strip().replace("  ", "/").strip("\n")

    while "//" in brewery_text_stripped:
        brewery_text_stripped = brewery_text_stripped.replace("//", "/")

    # print(brewery_text_stripped)

    briggs.addBeer(beer_name, brewery_text_stripped)

for beer in briggs.beer_list:
    print(beer)

russian_river = briggs.brewerySearch("Russian River Brewing")

print(russian_river)

num_rus = len(russian_river)

rus_list = ""

for item in russian_river:
    rus_list += str(item[0]) + ", "

notif_str = f"There are {num_rus} beers from Russian River on tap at Briggs: {rus_list}"

notifier.show_toast("Russian River Brewing",
                    notif_str,
                    )


