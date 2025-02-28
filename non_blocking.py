import aiohttp
import asyncio
import time
from bs4 import BeautifulSoup  # Import BeautifulSoup for HTML parsing

# List of URLs
urls = [
    "http://quotes.toscrape.com",
    "https://books.toscrape.com",
    "http://olympus.realpython.org/profiles/dionysus",
]


# Asynchronous function to fetch data
async def fetch_data(session, url):
    async with session.get(url) as response:
        text = await response.text()  # Get raw HTML response
        soup = BeautifulSoup(text, "html.parser")  # Parse HTML with BeautifulSoup
        title = soup.title.string if soup.title else "No Title Found"  # Extract page title
        return {"url": url, "title": title}  # Return a dictionary with URL and title


# Main asynchronous function
async def main():
    start_time = time.time()  # Track execution time

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]  # Create async tasks
        results = await asyncio.gather(*tasks)  # Run all tasks concurrently

        # Display fetched results
        for result in results:
            print(f"Fetched {result['url']}: {result['title']}")

    print(f"\nTotal time taken (Non-Blocking): {time.time() - start_time:.2f} seconds")


# Run the asynchronous event loop
asyncio.run(main())
