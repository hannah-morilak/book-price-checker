from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
import time

def search_target(item):
    # Open Target Home Page
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.target.com')

    # Search for book
    driver.find_element(by=By.ID, value='search').send_keys(item)
    driver.find_element(by=By.XPATH, value="//button[@type='submit']").click()
    time.sleep(3)

    # Open the first link
    possible_link = driver.find_element(by=By.PARTIAL_LINK_TEXT, value=item)
    possible_link.click()
    time.sleep(3)

    # Find dollar amount
    dollar_price = driver.find_element(by=By.XPATH, value="//span[@class='style__PriceFontSize-sc-1o3i6gc-0 kfATIS']")
    price = str(dollar_price.text)[1:]

    return "Target", price

if __name__ == "__main__":
    store, price = search_target("It Ends with Us")
    print("It Ends with Us: ${}".format(price))