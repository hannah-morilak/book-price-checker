import re, mechanicalsoup

# Barnes and Noble Search
def BarnesAndNobleSearch(book_title):
    url='https://www.barnesandnoble.com'
    headers = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Accept-Language': 'en-US, en;q=0.5'})

    # Creating the searchable book title
    searchable_title = book_title
    searchable_title.replace(" ", "%20")
    search_url = url + "/s/" + searchable_title

    # Opening the search page and finding all links
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(search_url, headers=headers)
    links = browser.page.find_all('a')

    # Searching for the correct link
    for link in links:  
        if re.search(book_title, str(link), re.IGNORECASE):
            book_endpoint = re.search("href=\"(.*);jsessionid", str(link))
            if book_endpoint != None:
                book_url = url + str(book_endpoint.group(1))
                break

    # Open the Book URL
    if book_endpoint != None:
        browser.open(book_url, headers=headers)
    current_price_with_formatting = browser.page.find(id='pdp-cur-price')
    price = re.search("</sup>(.*)</span>", str(current_price_with_formatting)).group(1)
    return "Barnes and Noble", price

if __name__ == "__main__":
    name, price = BarnesAndNobleSearch("It Ends with Us")
    print("It Ends with Us: ${}".format(price))