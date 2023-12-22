import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    articles = scrape_titles()
    return render_template('index.html', articles=articles)

def scrape_titles():
    site = 'https://www.wired.com'  # Change this URL to the desired website
    articles = []

    response = requests.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')

    for headline in soup.find_all('h2'):
        title = headline.text.strip()
        link = headline.a['href'] if headline.a else '#'
        articles.append({'title': title, 'link': link})

    return sorted(articles, key=lambda x: x['title'], reverse=True)

if __name__ == '__main__':
    app.run(debug=True)

