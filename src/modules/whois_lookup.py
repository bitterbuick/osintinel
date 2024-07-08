# src/modules/whois_lookup.py

import whois

class WhoisLookup:
    @staticmethod
    def get_whois(domain):
        try:
            w = whois.whois(domain)
            return w
        except Exception as e:
            print(f"Error performing WHOIS lookup for {domain}: {e}")
            return None

# Example usage
if __name__ == "__main__":
    domain = "example.com"
    whois_data = WhoisLookup.get_whois(domain)
    if whois_data:
        print(whois_data)

