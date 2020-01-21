import mechanicalsoup
import types
from collection import collection


def prices(browser_resp):
    class_name = "s-item__price"
    return browser_resp.soup.find_all("span", class_=class_name)


def names(browser_resp):
    class_name = "s-item__title"
    return browser_resp.soup.find_all("h3", class_=class_name)


def ship_from(browser_resp):
    class_name = "s-item__location s-item__itemLocation"
    return browser_resp.soup.find_all("span", class_=class_name)


def num_of_bids(browser_resp):
    class_name = "s-item__bids s-item__bidCount"
    return browser_resp.soup.find_all("span", class_=class_name)


def item_condition(browser_resp):
    class_name = "SECONDARY_INFO"
    return browser_resp.soup.find_all("span", class_=class_name)


def time_left(browser_resp):
    class_name = "s-item__time-left"
    return browser_resp.soup.find_all("span", class_=class_name)


def item_shipping(browser_resp):
    class_name = "s-item__shipping s-item__logisticsCost"
    return browser_resp.soup.find_all("span", class_=class_name)


def create_array(sup_finall):
    item = []
    for it in sup_finall:
        item.append(it.text)
    return item

def ebay_params(response):
    price = create_array(prices(response))
    name = create_array(names(response))
    ship_addr = create_array(ship_from(response))
    bid_cnt = create_array(num_of_bids(response))
    item_c = create_array(item_condition(response))
    
    return collection(name, price, ship_addr, bid_cnt, item_c)