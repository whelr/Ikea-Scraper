import urllib.request
import sys
from bs4 import BeautifulSoup

categories = [] #Create empty lists for categories and items
items = []
count = 0 #Create variable for counting items scraped.

allproducts = urllib.request.urlopen('https://www.ikea.com/us/catalog/allproducts/alphabetical/')
soup = BeautifulSoup(allproducts, 'html.parser')

for a in soup.find_all('a', href=True): #For every link on the ikea "All Products page"
	if a['href'].startswith('/us/en/catalog/categories/departments/'): #If the link is a category of products, and not already grabbed
		if a['href'] not in categories:
			categories.append(a['href']) #Add the category url to the list of categories.

for category in categories: #For each category of products, parse the page for product links.
	products = urllib.request.urlopen('https://www.ikea.com' + category)
	productSoup = BeautifulSoup(products, 'html.parser')
	for a in productSoup.find_all('a', href=True):
		if a['href'].startswith('/us/en/catalog/products/'): #For each item url, if its a product:
			if a['href'].endswith('?bvtab'): #Duplicate link, skip
				continue
			if a['href'] not in items: #If not already stored, save item url to list of items.
				items.append(a['href'])

#Create File, ikeaproducts.csv, with column headers id,name,price,description,url
filename = "ikeaproducts.csv"
f = open(filename,'w+') 
headers = "id,name,price,description,url\n"
f.write(headers)

for item in items: 
#for each item in the list we've scraped from ikea, until we've hit 1,000 items in our database
	if count >= 1000:
		break

	#url of item is website + stored part of url
	url = ('https://www.ikea.com' + item)
	itemInfo = '' #variable for item info we gather

	try:
		page = urllib.request.urlopen(url) #check to ensure we can access the item url, if bad url, go to next item
	except Exception as e:
		continue

	psoup = BeautifulSoup(page, 'html.parser')

	#Parse the item's product page and gather the information for itemN number, item name, price, and description
	id_box = psoup.find("div",attrs={"class":"floatLeft","id":"itemNumber"})
	name_box = psoup.find('span', attrs={'class':'productName'})
	price_box = psoup.find("div", attrs={'class':'priceContainer',"id":"priceContainer"})
	desc_box = psoup.find("div",attrs={"class":"salesArguments","id":"salesArg"})

	#If any of of the information is not available, we don't have a proper item, move on to the next item.
	if id_box is None or name_box is None or price_box is None or desc_box is None:
		continue

	#Cleanup of the parsed strings to get cleaner data
	id = id_box.text.strip()
	name = name_box.text.strip()
	name = ''.join(name.split())
	price = price_box.text.strip()
	price = price.split()[0]
	desc = desc_box.text.strip()

	#Compile the data into a string complying to the csv database headers, then write to csv file, and start new line
	itemInfo = (id + ",\"" + name + "\",\"" + price + '\",\"' + desc + '\",' + url)
	f.write(itemInfo + '\n')
	#increment the count so we can stop at 1000 for assignment purposes.
	count += 1

#close the file when finished.
f.close()
print("Finished scraping Ikea website to ikeaproducts.csv")