# src/config.py

import os

# Load .env before the class body reads the environment — class attributes are
# evaluated at import time, so loading afterwards left every credential as None.
try:
    from dotenv import load_dotenv
except ImportError:
    pass
else:
    load_dotenv()


class Config:
    # Twitter API credentials
    TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
    TWITTER_API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY')
    TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
    TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

    # LinkedIn credentials
    LINKEDIN_USERNAME = os.getenv('LINKEDIN_USERNAME')
    LINKEDIN_PASSWORD = os.getenv('LINKEDIN_PASSWORD')
