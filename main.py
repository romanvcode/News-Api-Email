import requests
from send_email import send_email

topic = "Tesla"
api_key = "2b5b2732f80e4fb9bc2bdbf3e257a2eb"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "sortBy=publishedAt&"
       "apiKey=2b5b2732f80e4fb9bc2bdbf3e257a2eb&"
       "language=en")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
text = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        text = ("Subject: Today`s news"
                + "\n" + text + article["title"] + "\n"
                + article["description"]
                + "\n" + article["url"] + 2 * "\n")

text = text.encode("utf-8")
send_email(message=text)
