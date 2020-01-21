from fake_useragent import UserAgent
import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()
browser.open("https://www.google.com/")

item_name = 'FPGA'
MAGIC_WORD = "price"

# Fill-in the form
browser.select_form('form[action="/search"]')
browser["q"] = item_name + " " + MAGIC_WORD

WEB_AGENT_NAME = "btnG"
resp = browser.submit_selected(btnName=WEB_AGENT_NAME)

results = resp.fin
print(resp.text)