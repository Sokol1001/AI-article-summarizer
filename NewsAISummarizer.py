from requests_html import HTML, HTMLSession
from transformers import pipeline
import tiktoken

session = HTMLSession()
summarize = pipeline("summarization")

link = input("Enter the link of an article from Global News:")
r = session.get(link)
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

headline = r.html.find('h1', first=True).text
print(headline)

summary =r.html.find('.l-article__text.js-story-text p')
    
all_paragraphs = [x.text for x in summary]
full_text = " ".join(all_paragraphs)

tokens = encoding.encode("full_text")

if(len(tokens) < 1024):
    res = summarize(full_text, max_new_tokens=500)
    print(res)
else:
    print("Your article is too big")