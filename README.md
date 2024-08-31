# Web Scraping and Word Frequency Project

This project is designed to scrape content from websites and analyze the frequency of words in the scraped data. It consists of two main Python scripts:

## Project Structure

1. **WebScrapingPython.py**:
   - **Purpose**: This script is responsible for web scraping and data extraction.
   - **Functionality**:
     - Uses libraries like `BeautifulSoup` and `requests` to gather data from websites.
     - Extracts textual content from the specified URLs.
     - Saves the scraped data for further processing.
   - **Dependencies**:
     - `BeautifulSoup` for parsing HTML.
     - `requests` for making HTTP requests.

2. **WordCount.py**:
   - **Purpose**: This script processes the data obtained from the `WebScrapingPython.py` script.
   - **Functionality**:
     - Reads the text data scraped from websites.
     - Calculates and displays the frequency of each word in the content.
     - Provides insights into the most common words on a web page.
   - **Dependencies**:
     - `collections.Counter` for counting word occurrences.
     - `re` for text processing.

## Installation

To get started with this project, you'll need to clone the repository and install the required Python libraries.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/gauravkdwivedi/Next-Hike-Project-1.git
   cd Next-Hike-Project-1