import requests
import time
from bs4 import BeautifulSoup  # Import BeautifulSoup for HTML parsing

# Fetch data from the given URL
def fetch_data(url):
    try:
        response = requests.get(url)  # Send HTTP GET request
        response.raise_for_status()   # Raise an error for HTTP errors

        # Return raw HTML content
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Process and extract meaningful data using BeautifulSoup
def process_data(data):
    if data:
        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(data, "html.parser")

        # Extract relevant information
        name = soup.find("h2")  # Name is in an <h2> tag
        favorite_color = soup.find("h3")  # Favorite color is in an <h3> tag

        # Extract the last modification date (if present)
        creation_date = soup.find("meta", attrs={"name": "date"})

        # Display extracted information
        print("\n--- Extracted Information ---")
        print(f"Name: {name.text.strip() if name else 'Not Found'}")
        print(f"Favorite Color: {favorite_color.text.strip() if favorite_color else 'Not Found'}")
        print(f"Creation Date: {creation_date['content'] if creation_date else 'Not Provided'}")
        print("----------------------------\n")

        print(data)  # Print full HTML content for debugging
    else:
        print("No data to process.")

# Main function to control the execution
def main():
    url = input("Enter the URL to fetch data from: ").strip()
    # url = "http://olympus.realpython.org/profiles/dionysus"  # Sample URL for testing

    iterations = 3  # Fetch data 3 times
    interval = 10   # Wait for 10 seconds between each fetch

    print("Starting data fetching process...\n")

    for i in range(iterations):
        print(f"Iteration {i + 1}:")

        # Fetch and process the data
        data = fetch_data(url)
        process_data(data)

        # Wait for the next iteration
        if i < iterations - 1:
            print(f"Waiting for {interval} seconds...\n")
            time.sleep(interval)

    print("\nData fetching process completed.")

# Entry point for the script
if __name__ == "__main__":
    main()
