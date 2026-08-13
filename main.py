import os
import requests

URL = "https://books.toscrape.com/catalogue/page-1.html"
CACHE_FILE = "cache/catalogue-page-1.html"
USER_AGENT = "FlyRankInternship_Assignment/1.0 (+https://github.com/Affaq7/the-polite-scraper)"

def fetch_and_cache():
    """Fetches a web page politely and caches it locally."""
    os.makedirs("cache", exist_ok=True)

    if os.path.exists(CACHE_FILE):
        print("CACHE HIT")
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            html = f.read()
            
    else:
        print("FETCH")
        headers = {"User-Agent": USER_AGENT}
        
        response = requests.get(URL, headers=headers, timeout=10)
        
        if response.status_code != 200:
            print(f"Failed to fetch page. Status code: {response.status_code}")
            return
            
        html = response.text
        
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            f.write(html)
            
    print(f"Response size: {len(html)} characters")

if __name__ == "__main__":
    fetch_and_cache()