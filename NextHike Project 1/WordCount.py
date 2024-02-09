# Word count
# Import the necessary libraries and files
from collections import Counter
import WebScappingPython

python_articles = WebScappingPython.get_latest_articles()
# Combine all article titles into a single string
all_titles = " ".join(python_articles)

# Split the text into words
words = all_titles.split()

# Create a Counter object to count word frequencies
word_count = Counter()

# Iterate through the words and count their frequencies
for word in words:
    # Remove punctuation and convert to lowercase to ensure consistency
    word = word.strip(".,!?'\"").lower()
    if word:
        word_count[word] += 1

# Sort the words by frequency in descending order
sorted_word_count = word_count.most_common()

# Print the sorted word count
for word, count in sorted_word_count:
    print(f"{word}: {count}")