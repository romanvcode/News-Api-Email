import requests
from send_email import send_email

api_key = "2b5b2732f80e4fb9bc2bdbf3e257a2eb"
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2023-07-26&sortBy=publishedAt&apiKey="
       "2b5b2732f80e4fb9bc2bdbf3e257a2eb")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
text = ""
for article in content["articles"]:
    text = text + article["title"] + "\n" + article["description"] + 2 * "\n"

text = text.encode("utf-8")
send_email(text)
