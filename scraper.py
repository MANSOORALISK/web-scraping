# Importing necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# Function to get HTML content from a URL
def get_html_content(url):
    response = requests.get(url)  # Sends a GET request to the URL
    return response.content  # Returns the raw HTML content

# Function to parse HTML content and extract quotes
def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')  # Parseing HTML content using BeautifulSoup
    quotes = []  # Initializing an empty list to store quotes
    for quote in soup.find_all('div', class_='quote'):  # Loops through all quote divs
        text = quote.find('span', class_='text').text  # Extracts the quote text
        author = quote.find('small', class_='author').text  # Extracts the author name
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]  # Extracts tags as a list of strings
        quotes.append({'text': text, 'author': author, 'tags': tags})  # Appends a dictionary to the quotes list
    return quotes  # Returns the list of quotes

# Function to save data to CSV
def save_to_csv(data, filename):
    df = pd.DataFrame(data)  # Converting the data to a pandas DataFrame
    df.to_csv(filename, index=False)  # Saves the DataFrame to a CSV file without the index

# Function to save data to JSON
def save_to_json(data, filename):
    with open(filename, 'w') as json_file:  # Opens a file in write mode
        json.dump(data, json_file, indent=4)  # Dumps the data as JSON with an indentation of 4 spaces

# Main function to orchestrate the web scraping
def main():
    url = 'http://quotes.toscrape.com'  # Defineing the URL to scrape
    html_content = get_html_content(url)  # Gets HTML content from the URL
    quotes = parse_html(html_content)  # Parsing the HTML content to extract quotes
    save_to_csv(quotes, 'quotes.csv')  # Saves the quotes to a CSV file
    save_to_json(quotes, 'quotes.json')  # Saves the quotes to a JSON file
    print("Data has been saved to quotes.csv and quotes.json")  # Prints a confirmation message

# Ensuring the main function runs only if the script is executed directly
if __name__ == '__main__':
    main()

'''
OUTPUT

Data has been saved to quotes.csv and quotes.json
'''
