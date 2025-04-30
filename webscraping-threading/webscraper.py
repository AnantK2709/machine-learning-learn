import threading
import requests
from bs4 import BeautifulSoup
from queue import Queue
import time

# This script demonstrates how to scrape multiple URLs concurrently using threading.
urls = [
    "https://www.octoparse.com/blog/scrape-data-from-multiple-urls",
    "https://www.sephora.sg/?ref=logo",
    "https://docs.praison.ai/mcp/ollama"
]

def fetch_content(url):
    try:
        print(f"Fetching {url}")
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        print(f"fetched content is {len(soup.text)} characters long")
        print(soup.text[:512])  # Print the first 100 characters of the content
        return soup
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
threads = []
for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
print("All threads have completed.")