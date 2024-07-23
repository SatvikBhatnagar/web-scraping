import pandas as pd
import requests
from bs4 import BeautifulSoup

import ip_rotator

# Initialize proxy for IP rotation
proxy = ip_rotator.Proxy(https=True)

# Initialize lists to store scraped data
Product_name = []
Prices = []
Description = []

# Loop through 10 pages of search results (could change it based on how many products you want)
# Each page has 24 products
for _ in range(10):
    # Construct the URL for each page
    url = ("https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace"
           "=FLIPKART&as-show=on&as=off&page=" + str(_))
    # Send a GET request to the URL
    r = requests.get(url)
    # If the request is not successful, change IP and retry until successful
    while r.status_code != 200:
        print("status code:", r.status_code)
        proxy.changeIp()
        r = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(r.text, "html.parser")
    # Find the main container with the product details
    box = soup.find("div", {"class": "DOjaWF gdgoEp"})

    # Extract and store product names
    names = box.find_all("div", {"class": "KzDlHZ"})
    for i in names:
        name = i.text
        Product_name.append(name)
    # print(Product_name) # Uncomment to debug product names

    # Extract and store product prices
    prices = box.find_all("div", {"class": "Nx9bqj _4b5DiR"})
    for i in prices:
        price = i.text
        Prices.append(price)
    # print(Prices) # Uncomment to debug prices

    # Extract and store product descriptions
    desc = box.find_all("ul", {"class": "G4BRas"})
    for i in desc:
        descrip_ = i.text
        Description.append(descrip_)
    # print(Description) # Uncomment to debug descriptions

# Create a DataFrame from the scraped data
df = pd.DataFrame({'Product_name': Product_name, 'Price': Prices, 'Description': Description})
# print(df) # Uncomment to debug the DataFrame

# Save the DataFrame to a CSV file
df.to_csv("flipkart_mobiles_under_50000.csv", index=False)
