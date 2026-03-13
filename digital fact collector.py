import requests
import json
import os
import time

FACTS_FILE = "facts.json"

def load_facts():
    """Load facts from the local JSON file. Returns a list of fact strings."""
    if not os.path.exists(FACTS_FILE):
        return []
    with open(FACTS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_facts(facts):
    """Save the list of facts to the local JSON file."""
    with open(FACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(facts, f, ensure_ascii=False, indent=2)

def fact_exists(fact, facts):
    """Check if a fact already exists in the list (case-insensitive)."""
    return fact.strip().lower() in (f.strip().lower() for f in facts)

def fetch_random_fact():
    """Fetch a random fact from the uselessfacts API and return it as a string."""
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    try:
        response = requests.get(url, params={"language": "en"})
        response.raise_for_status()
        data = response.json()
        return data.get("text", "No fact found.")
    except requests.RequestException as e:
        print("Error fetching fact:", e)
        return None

def add_fact_to_archive():
    """Fetch a fact, check for duplicates, and add it to the archive if unique."""
    facts = load_facts()
    fact = fetch_random_fact()
    if not fact:
        print("No fact fetched.")
        return False
    if fact_exists(fact, facts):
        print("Fact already exists in archive:", fact)
        return False
    else:
        facts.append(fact)
        save_facts(facts)
        print("New fact added:", fact)
        return True

def show_all_facts():
    """Display all facts in the archive."""
    facts = load_facts()
    if not facts:
        print("No facts in archive.")
    else:
        print("--- Fact Archive ---")
        for i, fact in enumerate(facts, 1):
            print(f"{i}. {fact}")

def auto_collect_facts(interval_seconds=60, max_iterations=None):
    """
    Periodically fetch and store unique facts.
    interval_seconds: time between fetches (default 60 seconds)
    max_iterations: number of times to fetch (None = infinite)
    """
    iteration = 0
    print(f"Starting automated fact collection every {interval_seconds} seconds. Press Ctrl+C to stop.")
    try:
        while True:
            added = add_fact_to_archive()
            iteration += 1
            if max_iterations and iteration >= max_iterations:
                print("Reached maximum iterations. Stopping.")
                break
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        print("\nFact collection stopped by user.")

if __name__ == "__main__":
    # To run once and show all facts, uncomment below:
    # add_fact_to_archive()
    # show_all_facts()

    # To run automated collection, adjust interval and max_iterations as needed:
    auto_collect_facts(interval_seconds=60, max_iterations=None)  # 60s interval, infinite loop
