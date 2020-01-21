import re
import mechanicalsoup
from parser import find_price_of_item
from bs4 import BeautifulSoup
from numpy import mean, absolute, median
from structure import structure
import status
import time

def get_prices_from_google(item_name):
    # Search for
    MAGIC_WORD = "price"

    # Connect to Google
    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://www.google.com/")

    # Fill-in the form
    browser.select_form('form[action="/search"]')
    browser["q"] = item_name + " " + MAGIC_WORD

    WEB_AGENT_NAME = "btnG"
    resp = browser.submit_selected(btnName=WEB_AGENT_NAME)

    item = resp.soup.find_all("div")
    
    print("Searcing for:", item_name)
    price_list = []

    # sleep in order to prevent Google bot detection
    time.sleep(1)
    
    for it in item:
        res = find_price_of_item(it.text)
        print(it.text)
        if res:
            price_list.append(res)
    print(price_list)
    if price_list:
        price = structure(mean(price_list), max(price_list), min(price_list))
        return price
    else:
        return status.FAILURE



#get_prices_from_google("Genuine ALTERA USB Blaster Rev C 6XX-40044R-0C")
