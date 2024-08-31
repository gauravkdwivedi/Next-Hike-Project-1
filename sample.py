# Import the required libraries
import requests
from bs4 import BeautifulSoup

# Define a function to get the titles of the latest articles on python.org
def get_latest_articles():
    # The URL of the Python.org website
    url = "https://www.python.org/"
    
    # Send an HTTP GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Initialize an empty list to store the titles of the latest articles
        article_titles = []

        # Use a CSS selector to locate the article titles within the blog widget
        for article in soup.select(".blog-widget li"):
            # Extract and strip the text content of the 'a' element
            title = article.a.get_text(strip=True)
            
            # Add the cleaned title to the list of article titles
            article_titles.append(title)

        # Return the list of article titles
        return article_titles
    else:
        # Print an error message if the request was unsuccessful
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        # Return an empty list to indicate that no articles were found
        return []

# Main script execution
if __name__ == "__main__":
    # Retrieve the latest article titles by calling the get_latest_articles() function
    python_articles = get_latest_articles()

    # Check if any articles were retrieved
    if python_articles:
        # Print a header for the list of articles
        print("Latest articles on Python.org:")
        
        # Iterate through the list of articles and print each one with its index
        for index, article in enumerate(python_articles, start=1):
            print(f"{index}. {article}")
    else:
        # Print a message if no articles were found
        print("No articles found.")