
import mechanicalsoup
from create_url import create_url
from collection import ebay_items, collection


def ebay_parser(search_string):
    url = create_url(search_string)

    # create browser object
    browser = mechanicalsoup.StatefulBrowser()
    response = browser.open(url)

    # Search only on items on Ebays page
    item_bar = response.soup.find("div", class_="srp-river-main clearfix")

    # create collection object
    Col = collection()

    # If no auction items found
    if not item_bar:
        return Col

    itm = item_bar.find_all("div", class_="s-item__wrapper clearfix")
    for item in itm:
        name = item.find("h3", class_="s-item__title").text
        raw_price = item.find("span", class_="s-item__price").text
        # shipping sometimes is not specified
        shipping = item.find(
            "span", class_="s-item__shipping s-item__logisticsCost")
        if shipping:
            shipping = shipping.text
        else:
            shipping = "Null"

        img_url = item.find("div", class_="s-item__image-wrapper").img["src"]
        bid_cnt = item.find(
            "span", class_="s-item__bids s-item__bidCount").text
        product_url = item.find("a", class_="s-item__link")["href"]
        # Item condition is optional
        item_condition = item.find("span", class_="SECONDARY_INFO")
        if item_condition:
            item_condition = item_condition.text
        else:
            item_condition = "Null"

        # assign search result to structure
        e_itm = ebay_items()
        e_itm.Names = name
        e_itm.Raw_prices = raw_price
        e_itm.Shipping = shipping
        e_itm.Img_url = img_url
        e_itm.Bid_cnt = bid_cnt
        e_itm.Item_condition = item_condition

        # save item in object vector
        Col.append(e_itm)

    return Col
