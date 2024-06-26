from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

def get_article_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # The Guardian uses <div> with class 'article-body-commercial-selector' for the main content
    article_body = soup.find('div', {'class': 'article-body-commercial-selector'})
    if not article_body:
        return "Could not find the article body."
    
    # Extract text content from paragraphs
    paragraphs = article_body.find_all('p')
    article_text = "\n\n".join([p.get_text() for p in paragraphs])
    
    return article_text

@app.route('/process_html', methods=['POST'])
def process_html():
    data = request.json
    html_content = data.get('html', '')
    print(html_content[:200])  # Print to console for debugging (truncated for readability)
    article_text = get_article_text(html_content)
    return jsonify(processed_content=article_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
