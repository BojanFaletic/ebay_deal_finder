#!/bin/python3

import mechanicalsoup
from collection import collection
from evaleuate import evaluate
from sql import write_results
from create_url import create_url
from ebay_parser_v2 import ebay_parser

# Searching for 
SEARCH_FOR = "FPGA"

# create collection of ebay items
O = ebay_parser(SEARCH_FOR)

# get actual price from google
evaluated_items = evaluate(O)


# write results to database
write_results(evaluated_items.status())