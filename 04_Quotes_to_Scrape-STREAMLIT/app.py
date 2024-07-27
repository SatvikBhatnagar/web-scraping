import streamlit as st
import requests
import pandas as pd
from bs4 import BeautifulSoup


# Function to get tags with caching
@st.cache_data
def get_tags():
    base_url = f'https://quotes.toscrape.com'
    response = requests.get(base_url)

    soup_ = BeautifulSoup(response.content, 'html.parser')
    tags_box = soup_.find('div', class_='col-md-4 tags-box')
    tag_elements = tags_box.find_all('a', class_='tag')
    tags_list = [tag_element.text.capitalize() for tag_element in tag_elements]
    return tags_list


# Fetch tags and display select box
tags = get_tags()
tag = st.selectbox('Choose a Genre', tags)

# Button to generate CSV
generate = st.button('Generate CSV')

# Fetch quotes based on selected tag
quotes_url = f'https://quotes.toscrape.com/tag/{tag.lower()}'
r = requests.get(quotes_url)
soup = BeautifulSoup(r.content, 'html.parser')
quotes = soup.find_all('div', class_='quote')

# List to store quotes
quote_file = []

# Parse and display quotes
for quote in quotes:
    text = quote.find('span', class_='text').text.strip('\"')
    cleaned_text = text.strip('“”').strip('\"').strip()
    author = quote.find('small', class_='author').text
    link = quote.find('a')['href']
    link = 'https://quotes.toscrape.com' + link

    st.success(text)
    st.markdown(f"<a href={link}>{author}</a>", unsafe_allow_html=True)

    quote_file.append([cleaned_text, author, link])

# Save to CSV when the button is clicked
if generate:
    try:
        df = pd.DataFrame(quote_file, columns=['Quote', 'Author', 'Link'])
        csv_path = f'{tag}.csv'
        df.to_csv(csv_path, index=False)
        st.toast(f'Saved successfully in {csv_path}')

    except Exception as e:
        st.dialog(f"error:{e}")
