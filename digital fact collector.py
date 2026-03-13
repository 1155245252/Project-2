import requests

def fetch_random_fact():
    """Fetch a random fact from the uselessfacts API and print it."""
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    try:
        response = requests.get(url, params={"language": "en"})
        response.raise_for_status()
        data = response.json()
        print("Random Fact:", data.get("text", "No fact found."))
    except requests.RequestException as e:
        print("Error fetching fact:", e)

if __name__ == "__main__":
    fetch_random_fact()
