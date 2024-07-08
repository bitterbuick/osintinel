# src/modules/twitter_scraper.py

import tweepy

class TwitterScraper:
    def __init__(self, api_key, api_secret_key, access_token, access_token_secret):
        auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def get_user_tweets(self, username, count=10):
        try:
            tweets = self.api.user_timeline(screen_name=username, count=count, tweet_mode="extended")
            return [tweet.full_text for tweet in tweets]
        except Exception as e:
            print(f"Error fetching tweets for user {username}: {e}")
            return None

# Example usage
if __name__ == "__main__":
    api_key = "your_api_key"
    api_secret_key = "your_api_secret_key"
    access_token = "your_access_token"
    access_token_secret = "your_access_token_secret"

    twitter_scraper = TwitterScraper(api_key, api_secret_key, access_token, access_token_secret)
    tweets = twitter_scraper.get_user_tweets("example_user")
    if tweets:
        print(tweets)

