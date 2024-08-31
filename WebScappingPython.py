# Import necessary libraries for web scraping
import requests
from bs4 import BeautifulSoup

# Function to fetch the latest article titles from Python.org
def fetch_latest_articles():
    url = "https://www.python.org/"  # URL of the Python.org website
    
    try:
        # Send an HTTP GET request to the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract the titles of the latest articles using a CSS selector
        article_titles = [article.a.get_text(strip=True) for article in soup.select(".blog-widget li")]
        
        return article_titles  # Return the list of article titles

    except requests.exceptions.RequestException as e:
        # Print an error message if the request failed
        print(f"Error fetching data from {url}: {e}")
        return []  # Return an empty list if an error occurred

# Main execution block
if __name__ == "__main__":
    # Retrieve the latest article titles
    python_articles = fetch_latest_articles()

    # Display the articles if any were retrieved
    if python_articles:
        print("Latest articles on Python.org:")
        for index, article in enumerate(python_articles, start=1):
            print(f"{index}. {article}")
    else:
        print("No articles found.")