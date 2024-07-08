# src/modules/dns_lookup.py

import socket

class DNSLookup:
    @staticmethod
    def get_ip(domain):
        try:
            ip = socket.gethostbyname(domain)
            return ip
        except socket.gaierror as e:
            print(f"Error resolving domain {domain}: {e}")
            return None

# Example usage
if __name__ == "__main__":
    domain = "example.com"
    ip = DNSLookup.get_ip(domain)
    if ip:
        print(f"The IP address of {domain} is {ip}")

