import requests

urls = [
    "http://quotes.toscrape.com",
    "https://books.toscrape.com",
    "http://olympus.realpython.org/profiles/dionysus",
]

for url in urls:
    response = requests.get(url)

    if response.status_code == 200:
        content_type = response.headers.get("Content-Type", "")

        if "application/json" in content_type:  # Check if response is JSON
            try:
                data = response.json()
                print("Title:", data.get("title", "No Title Found"))
            except requests.exceptions.JSONDecodeError:
                print(f"Error: Unable to parse JSON from {url}")
        else:
            print(f"Skipping {url}, response is not JSON.")
            print(response.text[:200])  # Print first 200 chars for debugging
    else:
        print(f"Error {response.status_code}: {response.text[:200]}")

