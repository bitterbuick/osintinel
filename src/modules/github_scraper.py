# src/modules/github_scraper.py

import requests

class GithubScraper:
    API_ROOT = "https://api.github.com"

    @staticmethod
    def get_profile(username):
        try:
            response = requests.get(
                f"{GithubScraper.API_ROOT}/users/{username}",
                headers={"Accept": "application/vnd.github+json"},
                timeout=10,
            )
            response.raise_for_status()
            user = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching GitHub profile {username}: {e}")
            return None

        return {
            "login": user.get("login"),
            "name": user.get("name"),
            "company": user.get("company"),
            "blog": user.get("blog"),
            "location": user.get("location"),
            "email": user.get("email"),
            "bio": user.get("bio"),
            "public_repos": user.get("public_repos"),
            "followers": user.get("followers"),
            "following": user.get("following"),
            "created_at": user.get("created_at"),
            "html_url": user.get("html_url"),
        }

    @staticmethod
    def get_repos(username, count=30):
        try:
            response = requests.get(
                f"{GithubScraper.API_ROOT}/users/{username}/repos",
                headers={"Accept": "application/vnd.github+json"},
                params={"sort": "updated", "per_page": min(count, 100)},
                timeout=10,
            )
            response.raise_for_status()
            repos = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching GitHub repos for {username}: {e}")
            return None

        return [
            {
                "name": repo.get("name"),
                "description": repo.get("description"),
                "language": repo.get("language"),
                "fork": repo.get("fork"),
                "stargazers_count": repo.get("stargazers_count"),
                "pushed_at": repo.get("pushed_at"),
                "html_url": repo.get("html_url"),
            }
            for repo in repos
        ]

# Example usage
if __name__ == "__main__":
    username = "octocat"
    profile = GithubScraper.get_profile(username)
    if profile:
        print(profile)
