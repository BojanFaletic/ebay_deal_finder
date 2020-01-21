from collection import collection,ebay_items
from structure import structure
from google_search import get_prices_from_google
from status import result 

def evaluate(ebay_items : collection):
  ranked_items = result()
  for item in ebay_items.items():
    google_value = get_prices_from_google(item.Names)
    if google_value:
      ranked_items.append(item.Names, item.Raw_prices, google_value.mean_)
  return ranked_items