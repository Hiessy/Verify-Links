import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import sys

def get_all_links(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return [a.get('href') for a in soup.find_all('a')]
    except Exception as e:
        print(f"Error while fetching links from {url}: {e}")
        return []

def is_valid(url):
    try:
        response = requests.head(url)
        return response.status_code < 400  # Check for all status codes >= 400
    except Exception as e:
        return False

def check_links(base_url):
    visited_links = set()
    links_to_visit = set()
    links_to_visit.add(base_url)

    while links_to_visit:
        current_url = links_to_visit.pop()
        if current_url in visited_links:
            continue

        #print(f"Checking link: {current_url}")

        if not is_valid(current_url):
            print(f"Broken link found: {current_url}")

        visited_links.add(current_url)
        links = get_all_links(current_url)

        for link in links:
            if link and not link.startswith('#'):
                absolute_link = urljoin(base_url, link)
                if urlparse(base_url).netloc in absolute_link:
                    links_to_visit.add(absolute_link)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_broken_links.py <website_url>")
        sys.exit(1)

    website_url = sys.argv[1]
    check_links(website_url)
