import streamlit as st
import requests

st.title("My Galaxy")

api_key = "2b5b2732f80e4fb9bc2bdbf3e257a2eb"
url = ("https://newsapi.org/v2/everything?"
       f"q=tesla&"
       "sortBy=publishedAt&"
       "apiKey=2b5b2732f80e4fb9bc2bdbf3e257a2eb")

response1 = requests.get(url)
data = response1.json()

st.write(data["title"])
