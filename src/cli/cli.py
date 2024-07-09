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
from src.modules.linkedin_scraper import LinkedinScraper
from src.modules.github_scraper import GithubScraper
from src.config import Config
from src.logger import logger
from src.report_generator import ReportGenerator
from src.username_generator import UsernameGenerator
import sherlock

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

    # Subparser for LinkedIn scraping
    linkedin_parser = subparsers.add_parser("linkedin", help="Scrape LinkedIn profile")
    linkedin_parser.add_argument("profile_url", type=str, help="LinkedIn profile URL to scrape")

    # Subparser for GitHub scraping
    github_parser = subparsers.add_parser("github", help="Scrape GitHub profile")
    github_parser.add_argument("username", type=str, help="GitHub username to scrape")

    # Subparser for username search
    username_parser = subparsers.add_parser("username_search", help="Generate and search usernames")
    username_parser.add_argument("first_name", type=str, help="First name")
    username_parser.add_argument("last_name", type=str, help="Last name")

    args = parser.parse_args()

    try:
        if args.command == "dns":
            ip = DNSLookup.get_ip(args.domain)
            if ip:
                logger.info(f"The IP address of {args.domain} is {ip}")
                ReportGenerator.save_report({"domain": args.domain, "ip": ip}, "dns_report.json")
            else:
                logger.error(f"Failed to get IP address for {args.domain}")

        elif args.command == "geo":
            geolocation = IPGeolocation.get_geolocation(args.ip)
            if geolocation:
                logger.info(geolocation)
                ReportGenerator.save_report({"ip": args.ip, "geolocation": geolocation}, "geo_report.json")
            else:
                logger.error(f"Failed to get geolocation for IP {args.ip}")

        elif args.command == "emails":
            html_content = WebRequest.fetch_html(args.url)
            if html_content:
                emails = EmailExtractor.extract_emails(html_content)
                if emails:
                    logger.info(f"Found emails: {emails}")
                    ReportGenerator.save_report({"url": args.url, "emails": emails}, "emails_report.json")
                else:
                    logger.warning(f"No emails found at {args.url}")
            else:
                logger.error(f"Failed to fetch HTML content from {args.url}")

        elif args.command == "whois":
            whois_data = WhoisLookup.get_whois(args.domain)
            if whois_data:
                logger.info(whois_data)
                ReportGenerator.save_report({"domain": args.domain, "whois": whois_data}, "whois_report.json")
            else:
                logger.error(f"Failed to perform WHOIS lookup for {args.domain}")

        elif args.command == "twitter":
            twitter_scraper = TwitterScraper(
                Config.TWITTER_API_KEY, Config.TWITTER_API_SECRET_KEY,
                Config.TWITTER_ACCESS_TOKEN, Config.TWITTER_ACCESS_TOKEN_SECRET
            )
            tweets = twitter_scraper.get_user_tweets(args.username, args.count)
            if tweets:
                logger.info(tweets)
                ReportGenerator.save_report({"username": args.username, "tweets": tweets}, "twitter_report.json")
            else:
                logger.error(f"Failed to fetch tweets for user {args.username}")

        elif args.command == "darkweb":
            page_content = DarkWebMonitor.fetch_tor_page(args.url)
            if page_content:
                logger.info(page_content)
                ReportGenerator.save_report({"url": args.url, "content": page_content}, "darkweb_report.json")
            else:
                logger.error(f"Failed to fetch Tor page {args.url}")

        elif args.command == "linkedin":
            linkedin_scraper = LinkedinScraper(Config.LINKEDIN_USERNAME, Config.LINKEDIN_PASSWORD)
            profile = linkedin_scraper.get_profile(args.profile_url)
            if profile:
                logger.info(profile)
                ReportGenerator.save_report({"profile_url": args.profile_url, "profile": profile}, "linkedin_report.json")
            else:
                logger.error(f"Failed to fetch LinkedIn profile {args.profile_url}")

        elif args.command == "github":
            profile = GithubScraper.get_profile(args.username)
            if profile:
                logger.info(profile)
                ReportGenerator.save_report({"username": args.username, "profile": profile}, "github_report.json")
            else:
                logger.error(f"Failed to fetch GitHub profile {args.username}")

        elif args.command == "username_search":
            usernames = UsernameGenerator.generate_usernames(args.first_name, args.last_name)
            results = {}
            for username in usernames:
                results[username] = sherlock.search(username, silent=True)
            logger.info(results)
            ReportGenerator.save_report({"first_name": args.first_name, "last_name": args.last_name, "results": results}, "username_search_report.json")

    except Exception as e:
        logger.exception(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

