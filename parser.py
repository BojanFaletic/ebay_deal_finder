
import re


def find_price_of_item(html_snippet):
    RE_PATTERN = r"\d*,\d*.\$"
    res = re.findall(RE_PATTERN, html_snippet)
    if (len(res) > 0):
        float_like_string = res[0][:-2].replace(',','.')
        # Empty string can still be number, possibly bug
        try:
            itm_price = float(float_like_string)
        except:
            return False
        return itm_price
    else:
        return False

