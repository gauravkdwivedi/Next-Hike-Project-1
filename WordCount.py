# Word Count Script
# This script counts the frequency of words in the titles of the latest articles from a web scraping module.

from collections import Counter
import WebScappingPython  # Ensure this module contains the `get_latest_articles` function

def count_word_frequencies(titles):
    """
    Count word frequencies from a list of article titles.

    Args:
        titles (list of str): List of article titles.

    Returns:
        list of tuple: Sorted list of tuples containing word and its frequency.
    """
    # Combine all titles into a single string
    all_titles = " ".join(titles)

    # Remove punctuation and convert to lowercase
    translator = str.maketrans("", "", ".,!?'\"")
    cleaned_titles = all_titles.translate(translator).lower()

    # Split the text into words
    words = cleaned_titles.split()

    # Count word frequencies
    word_count = Counter(words)

    # Return sorted word count
    return word_count.most_common()

def main():
    # Retrieve latest article titles
    python_articles = WebScappingPython.get_latest_articles()

    if python_articles:
        # Extract article titles from the data
        titles = [article[1] for article in python_articles]

        # Count word frequencies
        sorted_word_count = count_word_frequencies(titles)

        # Print the sorted word count
        print("Word frequencies in article titles:")
        for word, count in sorted_word_count:
            print(f"{word}: {count}")
    else:
        print("No articles found. Unable to perform word count.")

if __name__ == "__main__":
    main()