import requests
from bs4 import BeautifulSoup
# Send an HTTP GET request to the Wikipedia page
url = "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Italy"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract the introduction section
    introduction_paragraphs = soup.find_all("p")
    introduction = "\n".join([p.get_text() for p in introduction_paragraphs])
    
    print("Introduction:", introduction)
else:
    print("Failed to retrieve the web page.")

# Word count
from collections import Counter

# Text
introduction = introduction

# Split the text into words
words = introduction.split()

# Create a Counter object to count word frequencies
word_count = Counter()

# Iterate through the words and count their frequencies
for word in words:
    # Remove punctuation and convert to lowercase to ensure consistency
    word = word.strip(".,!?'\"").lower()
    word_count[word] += 1

# Sort the words by frequency in descending order
sorted_word_count = word_count.most_common()

# Print the sorted word count
for word, count in sorted_word_count:
    print(f"{word}: {count}")