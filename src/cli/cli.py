# src/cli/cli.py

import argparse
import sys
import os

# Ensure the src directory is in the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.append(parent_dir)

from src.modules.web_request import WebRequest
from src.modules.dns_lookup import DNSLookup
from src.modules.ip_geolocation import IPGeolocation
from src.modules.email_extractor import EmailExtractor
from src.modules.whois_lookup import WhoisLookup
from src.modules.twitter_scraper import TwitterScraper
from src.modules.dark_web_monitor import DarkWebMonitor

def main():
    parser = argparse.ArgumentParser(description="OSINT CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Subparser for DNS lookup
    dns_parser = subparsers.add_parser("dns", help="Perform a DNS lookup")
    dns_parser.add_argument("domain", type=str, help="Domain to look up")

    # Subparser for IP geolocation
    geo_parser = subparsers.add_parser("geo", help="Get geolocation for an IP address")
    geo_parser.add_argument("ip", type=str, help="IP address to geolocate")

    # Subparser for extracting emails
    email_parser = subparsers.add_parser("emails", help="Extract emails from a webpage")
    email_parser.add_argument("url", type=str, help="URL to fetch HTML content from")

    # Subparser for WHOIS lookup
    whois_parser = subparsers.add_parser("whois", help="Perform a WHOIS lookup")
    whois_parser.add_argument("domain", type=str, help="Domain to perform WHOIS lookup on")

    # Subparser for Twitter scraping
    twitter_parser = subparsers.add_parser("twitter", help="Scrape tweets from a Twitter user")
    twitter_parser.add_argument("username", type=str, help="Twitter username to scrape tweets from")
    twitter_parser.add_argument("--count", type=int, default=10, help="Number of tweets to scrape")

    # Subparser for Dark Web monitoring
    dark_web_parser = subparsers.add_parser("darkweb", help="Fetch a page from the dark web")
    dark_web_parser.add_argument("url", type=str, help="URL of the dark web page to fetch")

    args = parser.parse_args()

    if args.command == "dns":
        ip = DNSLookup.get_ip(args.domain)
        if ip:
            print(f"The IP address of {args.domain} is {ip}")

    elif args.command == "geo":
        geolocation = IPGeolocation.get_geolocation(args.ip)
        if geolocation:
            print(geolocation)

    elif args.command == "emails":
        html_content = WebRequest.fetch_html(args.url)
        if html_content:
            emails = EmailExtractor.extract_emails(html_content)
            if emails:
                print(f"Found emails: {emails}")

    elif args.command == "whois":
        whois_data = WhoisLookup.get_whois(args.domain)
        if whois_data:
            print(whois_data)

    elif args.command == "twitter":
        api_key = "your_api_key"
        api_secret_key = "your_api_secret_key"
        access_token = "your_access_token"
        access_token_secret = "your_access_token_secret"

        twitter_scraper = TwitterScraper(api_key, api_secret_key, access_token, access_token_secret)
        tweets = twitter_scraper.get_user_tweets(args.username, args.count)
        if tweets:
            print(tweets)

    elif args.command == "darkweb":
        page_content = DarkWebMonitor.fetch_tor_page(args.url)
        if page_content:
            print(page_content)

if __name__ == "__main__":
    main()

