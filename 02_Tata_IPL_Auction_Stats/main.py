import requests
from bs4 import BeautifulSoup
import pandas as pd


# Function to fetch the page content
def fetch_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.124 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
        return None


# Function to parse the page content
def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('div', class_='auction-grid-view mt-3')
    if not table:
        print("Table not found on the page.")
        return []

    teams = table.select('div.agv-main')
    teams_detail = []

    for team in teams:
        team_data = {}
        try:
            team_name = team.find('div', class_='agv-team-name').text
            team_data['Team Name'] = team_name

            funds_remaining = team.find('span', class_='fr-fund').text
            team_data['Funds Remaining (INR)'] = int(funds_remaining.replace('₹', '').replace(',', ''))

            span_elements = team.find_all('span', class_='fr-fund')
            if len(span_elements) > 1:
                overseas_players = span_elements[1].text
                team_data['Overseas Players'] = overseas_players
                total_players = span_elements[2].text
                team_data['Total Players'] = total_players

            teams_detail.append(team_data)
        except AttributeError as e:
            print(f"Error parsing team data: {e}")

    return teams_detail


# Function to save data to CSV
def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")


def main():
    url = 'https://www.iplt20.com/auction'
    html = fetch_page(url)
    if html:
        teams_detail = parse_page(html)
        save_to_csv(teams_detail, 'teams_detail.csv')


if __name__ == "__main__":
    main()
