# 02_Tata_IPL_Auction_Stats

This project scrapes IPL auction statistics from the [official IPL auction page](https://www.iplt20.com/auction) and extracts details about each team, including funds remaining, overseas players, and total players. The data is saved into a CSV file.

## Project Structure

- `ipl_auction_scraper.py`: Main script for scraping IPL auction data.
- `requirements.txt`: List of required Python packages.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repo.git
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

## Data Extraction

The script extracts the following information for each IPL team:
- **Team Name:** The name of the IPL team.
- **Funds Remaining (INR):** The remaining funds for the team, converted to an integer value.
- **Overseas Players:** The number of overseas players.
- **Total Players:** The total number of players.

## Contributing

Feel free to open issues or submit pull requests if you find any bugs or have suggestions for improvements.