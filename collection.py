class ebay_items:
    Names = ""
    Raw_prices = ""
    Shipping = ""
    Img_url = ""
    Bid_cnt = ""
    Product_url = ""
    Item_condition = ""


class collection:
    param = []

    def __init__(self):
        self.param.clear()

    def append(self, ebay_item : ebay_items):
        self.param.append(ebay_item)

    def names(self):
        names = []
        for itm in self.param:
            names.append(itm.Names)
        return names
    def items(self):
        return self.param


'''
    def append(self, names, prices, address, bids_cnt, items_c):
        tmp = self.t_type.copy()
        for i in range(0, len(names)):
            tmp["name"] = names[i]
            tmp["price"] = prices[i]
            tmp["address"] = address[i]
            tmp["bid_cnt"] = bids_cnt[i]
            tmp["item_condition"] = items_c[i]

            self.param.append(tmp)
'''
