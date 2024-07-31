# Web Scraper for UK Webuy

This project is a web scraper for extracting product information from the UK Webuy website. It uses Selenium to handle dynamic content and BeautifulSoup for parsing the HTML. The scraper retrieves details such as product titles, prices, image URLs, and product links, and then saves this data to a CSV file. It also downloads and stores product images locally.

## Project Structure

- `app.py`: Main script that performs web scraping and data extraction.
- `products.csv`: CSV file containing the scraped product details.
- `img/`: Directory where product images are saved.
- `README.md`: This README file.

## app.py

This script performs the following tasks:
- Sets up Selenium WebDriver with a headless Chrome browser.
- Fetches the webpage content and parses it with BeautifulSoup.
- Extracts product details including title, price, image URL, and product link.
- Downloads and saves product images to the `img` directory.
- Saves product details to a CSV file named `products.csv`.

### Overview of Functions

- `setUpDriver()`: Configures and initializes the Selenium WebDriver.
- `fetchProductDetails()`: Fetches and parses the product information from the webpage.
- `downloadImage()`: Downloads and saves the product images.
- `saveToCSV()`: Writes the product details to a CSV file.

## Installation

1. Clone the repository:
    ```bash
    git clone repository_link
    ```

2. Install the required packages:
    ```bash
    pip install selenium beautifulsoup4 requests
    ```

3. Download and install the ChromeDriver:
   Ensure you have ChromeDriver installed and it's available in your PATH. You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

## Usage

1. Run the script:
    ```bash
    python app.py
    ```

2. After running the script, the extracted product data will be saved in `products.csv` and product images will be stored in the `img` directory.

## Requirements

Ensure you have the following packages installed:
- `selenium`
- `beautifulsoup4`
- `requests`

## Contributing

Feel free to open issues or submit pull requests if you find any bugs or have suggestions for improvements.

## Acknowledgements

- Selenium WebDriver for handling dynamic web content.
- BeautifulSoup for parsing HTML.
- Requests for downloading images.
