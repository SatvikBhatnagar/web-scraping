# 03_Books_to_Scrape

This project scrapes book data from the website "Books to Scrape" and saves it into a CSV file. The data includes the title, star rating, and price of each book.

## Project Structure

- `main.py`: Main script for scraping book data.
- `books.csv`: The output CSV file with scraped data.
- `README.md`: This README file.

## 03_Books_to_Scrape.py

This script performs the following tasks:
- Fetches the webpage content of the book listing pages.
- Parses and extracts book details including the title, star rating, and price.
- Saves the extracted data to a CSV file.

### Overview of Functions

- `fetch_page(url)`: Fetches the page content from the provided URL.
- `scrape_books()`: Scrapes book data from the website and stores it in a DataFrame.
- `save_to_csv(data, filename)`: Saves the data to a CSV file.

### Data Files

- `books.csv`: Contains the scraped book data with columns for Title, Star Rating, and Price.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/SatvikBhatnagar/web-scraping/tree/main/03_Books_to_Scrape
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
        pip install -r requirements.txt
    ```

## Usage

1. Run the scraper script:
    ```bash
    cd web-scraping/03_Books_to_Scrape
    python main.py
    ```

2. After running the script, the extracted data will be saved in `books.csv` in the same directory.

## Requirements

Ensure you have the following packages installed:
- `requests`
- `beautifulsoup4`
- `pandas`

## Contributing

Feel free to open issues or submit pull requests if you find any bugs or have suggestions for improvements.

## Acknowledgements

- The website [Books to Scrape](https://books.toscrape.com/) for providing the data used in this project.
