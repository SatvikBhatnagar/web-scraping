# 02_Tata_IPL_Auction_Stats

This project scrapes IPL 2024 auction statistics from the [official IPL auction page](https://www.iplt20.com/auction/2024) and extracts details about each team, including funds remaining, overseas players, and total players. The data is saved into a CSV file.

## Project Structure

- `main.py`: Main script for scraping IPL 2024 auction data.
- `requirements.txt`: List of required Python packages.

## main.py

This script performs the following tasks:
- Fetches the auction webpage content.
- Parses and extracts team overviews, sold players, and unsold players.
- Saves the extracted data to CSV files.

### Overview of Functions

- `fetch_page(url)`: Fetches the page content from the provided URL.
- `overview(html)`: Parses and extracts team overview details.
- `sold_players(html)`: Parses and extracts details of sold players, including the team name.
- `unsold_players(html)`: Parses and extracts details of unsold players.
- `save_to_csv(data, filename)`: Saves the extracted data to a CSV file.
- `main()`: Main function to orchestrate the scraping and saving process.

### Data Files

- `overview_of_teams.csv`: Contains the overview of teams, including team name, funds remaining, overseas players, and total players.
- `sold_players.csv`: Contains details of sold players, including player name, nationality, type, price paid, and team name.
- `unsold_players.csv`: Contains details of unsold players.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/SatvikBhatnagar/web-scraping/tree/main/02_Tata_IPL_Auction_Stats
    cd your-repo/02_Tata_IPL_Auction_Stats
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the scraper script:
    ```bash
    python ipl_auction_scraper.py
    ```

2. After running the script, the extracted data will be saved in `teams_detail.csv` in the same directory.

## Requirements

The `requirements.txt` file includes the necessary Python packages for this project. Ensure you have the following packages installed:
- `requests`
- `beautifulsoup4`
- `pandas`

## Contributing

Feel free to open issues or submit pull requests if you find any bugs or have suggestions for improvements.