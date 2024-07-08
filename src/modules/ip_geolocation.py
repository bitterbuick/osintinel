# src/modules/ip_geolocation.py

import requests

class IPGeolocation:
    @staticmethod
    def get_geolocation(ip):
        try:
            response = requests.get(f"https://ipinfo.io/{ip}/json")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching geolocation for IP {ip}: {e}")
            return None

# Example usage
if __name__ == "__main__":
    ip = "8.8.8.8"
    geolocation = IPGeolocation.get_geolocation(ip)
    if geolocation:
        print(geolocation)

