# src/modules/web_request.py

import requests
from bs4 import BeautifulSoup

class WebRequest:
    @staticmethod
    def fetch_html(url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching URL {url}: {e}")
            return None

    @staticmethod
    def parse_html(html):
        return BeautifulSoup(html, 'html.parser')

# Example usage
if __name__ == "__main__":
    url = "https://example.com"
    html_content = WebRequest.fetch_html(url)
    if html_content:
        soup = WebRequest.parse_html(html_content)
        print(soup.prettify())

