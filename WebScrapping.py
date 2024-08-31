import requests
from bs4 import BeautifulSoup
from collections import Counter
import string

# Function to fetch the introduction section from a Wikipedia page
def fetch_introduction(url):
    try:
        # Send an HTTP GET request to the specified URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract all paragraphs in the introduction section
        introduction_paragraphs = soup.find_all("p")
        
        # Join the text from all paragraphs into a single string
        introduction = "\n".join([p.get_text() for p in introduction_paragraphs])
        
        return introduction
    
    except requests.exceptions.RequestException as e:
        # Handle errors during the HTTP request
        print(f"Error fetching the page: {e}")
        return None

# Function to count word frequencies in a text
def count_word_frequencies(text):
    # Remove punctuation and convert the text to lowercase
    translator = str.maketrans("", "", string.punctuation)
    words = text.translate(translator).lower().split()

    # Use Counter to count the frequency of each word
    word_count = Counter(words)
    
    # Sort the words by frequency in descending order
    sorted_word_count = word_count.most_common()
    
    return sorted_word_count

# Main execution block
if __name__ == "__main__":
    # Wikipedia URL for the COVID-19 pandemic in Italy page
    url = "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Italy"
    
    # Fetch the introduction section of the Wikipedia page
    introduction = fetch_introduction(url)
    
    if introduction:
        # Display the introduction text
        print("Introduction:\n", introduction)
        
        # Count and display word frequencies in the introduction
        word_frequencies = count_word_frequencies(introduction)
        print("\nWord Frequencies:")
        for word, count in word_frequencies:
            print(f"{word}: {count}")
    else:
        print("Failed to retrieve the introduction.")