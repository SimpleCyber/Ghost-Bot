from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup
import time  # Simulate processing time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    user_message = request.form.get('message')
    
    try:
        # Simulate a response generation process (mock GPT response)
        response_text = f"Your message: '{user_message}' received! Processing the webpage content for: {url}"
        time.sleep(2)  # Simulating "thinking" time

        # Fetch and scrape the URL content
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        scraped_content = soup.prettify()

        return render_template('result.html', url=url, message=user_message, response=response_text, content=scraped_content)
    except requests.exceptions.RequestException as e:
        error_message = f"Error: Could not fetch the URL - {e}"
        return render_template('result.html', url=url, message=user_message, error=error_message)

if __name__ == '__main__':
    app.run(debug=True)
