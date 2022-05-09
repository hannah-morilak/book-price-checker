from BarnesAndNoble import search_barnes_and_noble
from Target import search_target
from Amazon import search_amazon


def SearchForCheapest(title):
    cheapest = {
    "Price" : 10000000,
    "Seller" : "Ur mom"
    }

    # Barnes and Noble
    seller, price = search_barnes_and_noble(title)
    if float(price) < float(cheapest["Price"]):
        cheapest["Price"] = price
        cheapest["Seller"] = seller

    # Amazon
    seller, price = search_amazon(title)
    if float(price) < float(cheapest["Price"]):
        cheapest["Price"] = price
        cheapest["Seller"] = seller
    elif float(price) == float(cheapest["Price"]):
        cheapest["Seller"] = "{} or {}".format(cheapest["Seller"], seller)

    # Target
    seller, price = search_target(title)
    if float(price) < float(cheapest["Price"]):
        cheapest["Price"] = price
        cheapest["Seller"] = seller
    elif float(price) == float(cheapest["Price"]):
        cheapest["Seller"] = "{} or {}".format(cheapest["Seller"], seller)

    print("The Cheapest Copy of {} can be found at {} for ${}".format(title, cheapest["Seller"], cheapest["Price"]))
    return cheapest["Seller"], cheapest["Price"]



if __name__ == "__main__":
    SearchForCheapest("It Ends with Us")