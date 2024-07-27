# Quotes Scraper

This project scrapes quotes from the website [Quotes to Scrape](https://quotes.toscrape.com/) based on selected genres and saves the data into a CSV file. The data includes the quote text, author, and a link to the author's page.

## Project Structure

- `app.py`: Main script for scraping quotes.
- `README.md`: This README file.
- `requirements.txt`: List of required Python packages.

## app.py

This script performs the following tasks:
- Fetches the main page content to retrieve available genres.
- Displays a select box for the user to choose a genre.
- Fetches the webpage content for the selected genre.
- Parses and extracts quotes, authors, and links to author pages.
- Displays the extracted quotes and authors.
- Saves the extracted data to a CSV file when the button is clicked.

### Overview of Functions

- `get_tags()`: Fetches the available genres from the main page.
- `fetch_quotes(tag)`: Fetches and parses quotes based on the selected genre.
- `save_to_csv(data, filename)`: Saves the extracted data to a CSV file.

### Data Files

- `Books.csv`: Contains the scraped quotes data for the "Books" genre.
- `Humor.csv`: Contains the scraped quotes data for the "Humor" genre.
- `Love.csv`: Contains the scraped quotes data for the "Love" genre.
- `Reading.csv`: Contains the scraped quotes data for the "Reading" genre.
- `Truth.csv`: Contains the scraped quotes data for the "Truth" genre.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/SatvikBhatnagar/web-scraping
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    pip install streamlit
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    cd 04_Quotes_to_Scrape-STREAMLIT
    streamlit run app.py
    ```

2. Select a genre from the dropdown menu.
3. Click the "Generate CSV" button to save the quotes to a CSV file.

## Requirements

Ensure you have the following packages installed:
- `streamlit`
- `requests`
- `beautifulsoup4`
- `pandas`

## Contributing

Feel free to open issues or submit pull requests if you find any bugs or have suggestions for improvements.

## Acknowledgements

- The website [Quotes to Scrape](https://quotes.toscrape.com/) for providing the data used in this project.
