# tests/test_github_scraper.py

import unittest
from src.modules.github_scraper import GithubScraper

class TestGithubScraper(unittest.TestCase):
    def test_get_profile(self):
        profile = GithubScraper.get_profile("octocat")
        self.assertIsNotNone(profile)
        self.assertIn("login", profile)
        self.assertEqual(profile["login"], "octocat")

if __name__ == "__main__":
    unittest.main()

