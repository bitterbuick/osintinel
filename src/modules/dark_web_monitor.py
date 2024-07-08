# src/modules/dark_web_monitor.py

import requests

class DarkWebMonitor:
    @staticmethod
    def fetch_tor_page(url):
        try:
            proxies = {
                "http": "socks5h://127.0.0.1:9050",
                "https": "socks5h://127.0.0.1:9050"
            }
            response = requests.get(url, proxies=proxies)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching Tor page {url}: {e}")
            return None

# Example usage
if __name__ == "__main__":
    url = "http://example.onion"
    page_content = DarkWebMonitor.fetch_tor_page(url)
    if page_content:
        print(page_content)

