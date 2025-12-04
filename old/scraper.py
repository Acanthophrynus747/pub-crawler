from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#TODO: add into raspberry pi, using GPIO pins to light up indicator sign

pliny = False

service = Service(executable_path="chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.savorolympia.com/briggs-taphouse#02")

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "item-name"))
)

item_names = driver.find_elements(By.CLASS_NAME, "item-name")

breweries = driver.find_elements(By.CLASS_NAME, "brewery")

items = driver.find_elements(By.CLASS_NAME, "item")

# for item in items:
#     item_text = item.text
#     print(item_text)
#     if "PLINY" in item_text:
#         # print("pliny!")
#         pliny = True
#     # print(type(item))

for item_name in item_names:
    item_name_text = item_name.text
    print(item_name_text)
    if "PLINY" in item_name_text:
        # print("pliny!")
        pliny = True

# for brewery in breweries:
#     print(brewery.text)

driver.quit()

if pliny == True:
    print("Pliny the Elder is on tap!")