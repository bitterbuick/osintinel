# src/modules/linkedin_scraper.py

from linkedin_api import Linkedin

class LinkedinScraper:
    def __init__(self, username, password):
        self.api = Linkedin(username, password)

    def get_profile(self, profile_url):
        try:
            profile_id = profile_url.split('/')[-1]
            profile = self.api.get_profile(profile_id)
            return profile
        except Exception as e:
            print(f"Error fetching LinkedIn profile {profile_url}: {e}")
            return None

# Example usage
if __name__ == "__main__":
    username = "your_linkedin_username"
    password = "your_linkedin_password"
    profile_url = "https://www.linkedin.com/in/example-profile"

    linkedin_scraper = LinkedinScraper(username, password)
    profile = linkedin_scraper.get_profile(profile_url)
    if profile:
        print(profile)

