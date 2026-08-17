# src/cli/cli.py

import argparse
import sys
import os

# Ensure the src directory is in the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
sys.path.append(parent_dir)

# Modules are imported inside each command branch rather than at import time.
# The twitter, linkedin and whois modules pull in optional third-party packages
# (and in some cases need API credentials); importing them eagerly meant a
# missing optional dependency broke every command, including --help.


def build_parser():
    parser = argparse.ArgumentParser(prog="osintinel", description="OSINT CLI Tool")
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
    github_parser.add_argument("--repos", action="store_true", help="List public repositories instead of the profile")

    return parser


def missing_dependency(exc, package):
    print(f"This command needs the '{package}' package, which is not installed: {exc}")
    print(f"Install it with:  pip install {package}")
    return 1


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        return 0

    if args.command == "dns":
        from src.modules.dns_lookup import DNSLookup
        ip = DNSLookup.get_ip(args.domain)
        if ip:
            print(f"The IP address of {args.domain} is {ip}")

    elif args.command == "geo":
        from src.modules.ip_geolocation import IPGeolocation
        geolocation = IPGeolocation.get_geolocation(args.ip)
        if geolocation:
            print(geolocation)

    elif args.command == "emails":
        from src.modules.web_request import WebRequest
        from src.modules.email_extractor import EmailExtractor
        html_content = WebRequest.fetch_html(args.url)
        if html_content:
            emails = EmailExtractor.extract_emails(html_content)
            if emails:
                print(f"Found emails: {emails}")

    elif args.command == "whois":
        try:
            from src.modules.whois_lookup import WhoisLookup
        except ImportError as e:
            return missing_dependency(e, "python-whois")
        whois_data = WhoisLookup.get_whois(args.domain)
        if whois_data:
            print(whois_data)

    elif args.command == "twitter":
        try:
            from src.modules.twitter_scraper import TwitterScraper
        except ImportError as e:
            return missing_dependency(e, "tweepy")
        from src.config import Config
        twitter_scraper = TwitterScraper(
            Config.TWITTER_API_KEY, Config.TWITTER_API_SECRET_KEY,
            Config.TWITTER_ACCESS_TOKEN, Config.TWITTER_ACCESS_TOKEN_SECRET
        )
        tweets = twitter_scraper.get_user_tweets(args.username, args.count)
        if tweets:
            print(tweets)

    elif args.command == "darkweb":
        from src.modules.dark_web_monitor import DarkWebMonitor
        page_content = DarkWebMonitor.fetch_tor_page(args.url)
        if page_content:
            print(page_content)

    elif args.command == "linkedin":
        try:
            from src.modules.linkedin_scraper import LinkedinScraper
        except ImportError as e:
            return missing_dependency(e, "linkedin-api")
        from src.config import Config
        linkedin_scraper = LinkedinScraper(Config.LINKEDIN_USERNAME, Config.LINKEDIN_PASSWORD)
        profile = linkedin_scraper.get_profile(args.profile_url)
        if profile:
            print(profile)

    elif args.command == "github":
        from src.modules.github_scraper import GithubScraper
        if args.repos:
            result = GithubScraper.get_repos(args.username)
        else:
            result = GithubScraper.get_profile(args.username)
        if result:
            print(result)

    return 0


if __name__ == "__main__":
    sys.exit(main())
