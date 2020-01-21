def create_url(search_for):
  search_str = search_for.replace(' ','+')
  return "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + search_str + "&_sacat=0&rt=nc&LH_Auction=1"