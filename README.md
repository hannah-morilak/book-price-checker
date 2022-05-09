# book-price-checker
Uses web-scraping to check common book sellers for the cheapest price


## Desciption
Using a combination of Selenium and BeautifulSoup, this program checks the following book sellers for the cheapest price:
- Barnes and Nobles
- Target 
- Amazon

The overall goal of this project is to be able to open up my iPhone 13, and run a shortcut which will send an HTTP request to a machine and recieve information about which bookseller is the cheapest.

This is so that while I am out at second hand book stores, I can quickly check for the lowest price available and compare that to a used book price. 

## Tasks
- [x] Setup Barnes & Noble Web Scraping
- [x] Setup Target Web Scraping
- [x] Setup Amazon Web Scraping
- [x] Setup general file to check all stores and return cheapest price + store
- [ ] Create back-end to recieve HTTP requests and return cheapest price + store
- [ ] Setup iPhone shortcut to send HTTP request

To be added later on:  
- [ ] Create TBR list
- [ ] Create endpoint to add, remove and check TBR
- [ ] Run program on a schedule and alert me if a price lowers