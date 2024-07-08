# src/config.py

import os

class Config:
    # Twitter API credentials
    TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
    TWITTER_API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY')
    TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
    TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

    # LinkedIn credentials
    LINKEDIN_USERNAME = os.getenv('LINKEDIN_USERNAME')
    LINKEDIN_PASSWORD = os.getenv('LINKEDIN_PASSWORD')

# Load environment variables from a .env file if necessary
from dotenv import load_dotenv
load_dotenv()

