# src/modules/github_scraper.py

import requests

class GithubScraper:
    @staticmethod
    def get_profile(username):
        url = f"https://api.github.com/users/{username}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching GitHub profile {username}: {e}")
            return None

# Example usage
if __name__ == "__main__":
    username = "octocat"
    profile = GithubScraper.get_profile(username)
    if profile:
        print(profile)

