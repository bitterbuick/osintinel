# src/modules/twitter_scraper.py

import tweepy

class TwitterScraper:
    def __init__(self, bearer_token):
        self.client = tweepy.Client(bearer_token=bearer_token)

    def get_user_profile(self, username):
        try:
            user = self.client.get_user(username=username, user_fields=['created_at', 'description', 'location', 'public_metrics', 'verified'])
            user_profile = {
                'id': user.data.id,
                'name': user.data.name,
                'username': user.data.username,
                'created_at': user.data.created_at,
                'description': user.data.description,
                'location': user.data.location,
                'followers_count': user.data.public_metrics['followers_count'],
                'following_count': user.data.public_metrics['following_count'],
                'tweet_count': user.data.public_metrics['tweet_count'],
                'listed_count': user.data.public_metrics['listed_count'],
                'verified': user.data.verified
            }
            return user_profile

        except tweepy.TweepyException as e:
            print(f"Error fetching profile for user @{username}: {e}")
            return None

# Example usage
if __name__ == "__main__":
    import os
    from dotenv import load_dotenv

    load_dotenv()

    twitter_scraper = TwitterScraper(
        bearer_token=os.getenv('TWITTER_BEARER_TOKEN')
    )
    profile = twitter_scraper.get_user_profile("mountain_goats")
    if profile:
        print(profile)

