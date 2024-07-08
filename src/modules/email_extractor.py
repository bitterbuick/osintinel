# src/modules/email_extractor.py

import re

class EmailExtractor:
    @staticmethod
    def extract_emails(html):
        email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_regex, html)
        return emails

# Example usage
if __name__ == "__main__":
    html_content = "<html><body>Contact us at info@example.com and support@example.org</body></html>"
    emails = EmailExtractor.extract_emails(html_content)
    if emails:
        print(f"Found emails: {emails}")

