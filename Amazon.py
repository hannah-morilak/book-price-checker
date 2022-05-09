from selenium import webdriver
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selectorlib import Extractor
from itertools import permutations
import requests
import json
import time

def search_amazon(item):
    # Open amazon homepage
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.amazon.com')

    # Search for book name
    driver.find_element(by=By.ID, value='twotabsearchtextbox').send_keys(item)
    driver.find_element(by=By.ID, value="nav-search-submit-text").click()

    # Click First Element
    possible_link = driver.find_element(by=By.PARTIAL_LINK_TEXT, value=item)
    possible_link.click()

    # Find price and return
    price = driver.find_element(by=By.ID, value="price").text
    price = str(price)
    price = price[1:]
    return "Amazon", price

if __name__ == "__main__":
    store, price = search_amazon("It Ends with Us")
    print("It Ends with Us: ${}".format(price))