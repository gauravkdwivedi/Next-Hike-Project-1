# Import the necessary liabraries
import requests
from bs4 import BeautifulSoup

# Define a function to get the titles of the latest articles on python.org
def get_latest_articles():
    # The URL of the Python.org website
    url = "https://www.python.org/"
    
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Create an empty list to store the titles of the latest articles
        latest_articles = []

        # Use a CSS selector to locate article titles within list items
        for article in soup.select(".blog-widget li"):
            # Extract and strip the text content of the 'a' element
            title = article.a.text.strip()
            
            # Add the title to the list of latest articles
            latest_articles.append(title)

        # Return the list of latest article titles
        return latest_articles
    else:
        # Print an error message if the request was not successful
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        # Return an empty list to indicate no articles were found
        return []

# Main script execution
if __name__ == "__main__":
    # Call the get_latest_articles() function to retrieve article titles
    python_articles = get_latest_articles()

    # Check if there are articles in the list
    if python_articles:
        # Print the header
        print("Latest article in the python section:")       
        # Loop through the articles and print each one with an index
        for index, article in enumerate(python_articles, 1):
            print(f"{index}. {article}")
    else:
        # Print a message if no articles were found
        print("No article found")
