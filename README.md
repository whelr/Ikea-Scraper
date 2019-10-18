# Web Scraper for Ikea Products

## Introduction

Database is built from a web-scraper that scraped all products listed on IKEA’s US website. The scraped data from each product includes the product number, product name, description, and the URL to the item. The purpose of collecting this database is to allow any app or system to access the entire IKEA catalog without navigating the website one page at a time.

### Prerequisites

```
Python3
urllib
BeautifulSoup
```

### Running

Python3 installed with BeautifulSoup package installed.

Using terminal, cd to directory of IkeaScrape.py and execute file.

```
python3 IkeaScrape.py
```

## Data Summary

For the purposes of this assignment 1,000 tuples are included in the database. However, if the limit is removed from the source code it would have no problem handling the 8,300 products on IKEA’s website.

Headers for csv database are: id, name, price, description, url

The id is pulled from ikea’s system, which is in the format xxx.xxx.xx
The name is from ikea’s naming system, which are words from Scandinavian culture
The product description is the description given to the item by IKEA, likewise with price.




