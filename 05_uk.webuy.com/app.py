import os
import csv
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Create 'img' directory if it doesn't exist
if not os.path.exists('img'):
    os.makedirs('img')

# Set up Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)

URL = 'https://uk.webuy.com/search?productLineId=50&productLineName'
driver.get(URL)

# Wait for the product cards to be present
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "search-product-card"))
)

html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, 'html.parser')
product_cards = soup.find_all('div', class_='search-product-card')

# Open CSV file for writing
with open('products.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['Title', 'Price', 'Image Path', 'Product Link'])

    for product in product_cards:
        try:
            # Extract product title
            title_tag = product.find('div', class_='card-title')
            title = title_tag.text.strip() if title_tag else 'N/A'

            # Extract product price
            price_tag = product.find('p', class_='product-main-price')
            price = price_tag.text.strip() if price_tag else 'N/A'

            # Extract product image URL
            img_tag = product.find('div', class_='thumbnail').find('img')
            img_url = img_tag['src'] if img_tag else 'N/A'

            # Extract product link
            link_tag = product.find('a')
            product_link = 'https://uk.webuy.com' + link_tag['href'] if link_tag else 'N/A'

            # Download and save the image
            if img_url != 'N/A':
                try:
                    img_data = requests.get(img_url).content
                    img_name = img_url.split('/')[-1]
                    img_path = os.path.join('img', img_name)
                    with open(img_path, 'wb') as img_file:
                        img_file.write(img_data)
                except Exception as e:
                    img_path = 'N/A'
                    print(f"Error downloading image {img_url}: {e}")
            else:
                img_path = 'N/A'

            # Write the product details to the CSV file
            writer.writerow([title, price, img_path, product_link])

            # Optional: Introduce a delay between requests
            time.sleep(1)

        except Exception as e:
            print(f"Error processing product: {e}")
