# Web Scraping and Word Frequency Project

This project is designed to scrape content from websites and analyze the frequency of words in the scraped data. It consists of two main Python scripts:

## Project Structure

### 1. **WebScrapingPython.py**
   - **Purpose**: This script is responsible for web scraping and data extraction.
   - **Functionality**:
     - Uses libraries like `BeautifulSoup` and `requests` to gather data from websites.
     - Extracts textual content from the specified URL (Python.org in this case).
     - Returns the titles of the latest articles found on the webpage.
   - **Dependencies**:
     - `BeautifulSoup` for parsing HTML.
     - `requests` for making HTTP requests.

### 2. **WordCount.py**
   - **Purpose**: This script processes the data obtained from the `WebScrapingPython.py` script.
   - **Functionality**:
     - Retrieves the latest article titles using the `WebScrapingPython` module.
     - Counts and displays the frequency of each word found in the article titles.
     - Provides insights into the most common words in the titles.
   - **Dependencies**:
     - `collections.Counter` for counting word occurrences.

## Installation

To get started with this project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/gauravkdwivedi/Next-Hike-Project-1.git
   cd Next-Hike-Project-1