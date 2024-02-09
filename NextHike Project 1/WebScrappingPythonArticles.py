import requests
from bs4 import BeautifulSoup

def get_latest_articles():
    url = "https://www.python.org/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        latest_articles = []

        for article_index, article in enumerate(soup.select(".blog-widget li"), 1):
            title = article.a.text.strip()
            latest_articles.append((article_index, title, article.a["href"]))

        return latest_articles
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return []

def get_article_by_number(article_number):
    articles = get_latest_articles()
    
    if articles:
        try:
            article_number = int(article_number)
            if 1 <= article_number <= len(articles):
                selected_article = articles[article_number - 1]
                article_title = selected_article[1]
                article_url = selected_article[2]
                
                article_response = requests.get(article_url)
                if article_response.status_code == 200:
                    article_soup = BeautifulSoup(article_response.text, "html.parser")
                    content = article_soup.find("div", class_="article-content")
                    if content:
                        article_content = content.get_text()
                    else:
                        article_content = "Content not found."

                    return {
                        "title": article_title,
                        "content": article_content
                    }
                else:
                    return {
                        "title": "Failed to retrieve article content",
                        "content": f"Status code: {article_response.status_code}"
                    }
            else:
                return {
                    "title": "Invalid article number",
                    "content": "Please enter a valid article number."
                }
        except ValueError:
            return {
                "title": "Invalid input",
                "content": "Please enter a valid integer article number."
            }
    else:
        return {
            "title": "No articles found",
            "content": "No articles available to choose from."
        }

if __name__ == "__main__":
    python_articles = get_latest_articles()

    if python_articles:
        print("Latest articles in the python section:")
        for index, article in enumerate(python_articles, 1):
            print(f"{index}. {article[1]}")

        article_number = input("Enter the number of the article you want to retrieve: ")
        article_data = get_article_by_number(article_number)

        print(f"Title: {article_data['title']}")
        print("Content:")
        print(article_data['content'])
    else:
        print("No articles found")