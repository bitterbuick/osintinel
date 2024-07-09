# src/modules/twitter_scraper.py

import tweepy

class TwitterScraper:
    def __init__(self, bearer_token):
        self.client = tweepy.Client(bearer_token)

    def get_user_tweets(self, username, count=10):
        try:
            user = self.client.get_user(username=username)
            user_id = user.data.id

            tweets = self.client.get_users_tweets(id=user_id, max_results=count)

            tweet_list = []
            for tweet in tweets.data:
                tweet_list.append({
                    'id': tweet.id,
                    'text': tweet.text,
                    'created_at': tweet.created_at,
                    'username': username
                })
            return tweet_list

        except tweepy.TweepyException as e:
            print(f"Error fetching tweets for user @{username}: {e}")
            return None

# Example usage
if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    load_dotenv()

    twitter_scraper = TwitterScraper(
        bearer_token=os.getenv('TWITTER_BEARER_TOKEN')
    )
    tweets = twitter_scraper.get_user_tweets("mountain_goats")
    if tweets:
        print(tweets)

