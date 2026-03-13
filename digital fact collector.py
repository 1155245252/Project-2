import requests
import json
import os

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
        return
    if fact_exists(fact, facts):
        print("Fact already exists in archive:", fact)
    else:
        facts.append(fact)
        save_facts(facts)
        print("New fact added:", fact)

def show_all_facts():
    """Display all facts in the archive."""
    facts = load_facts()
    if not facts:
        print("No facts in archive.")
    else:
        print("--- Fact Archive ---")
        for i, fact in enumerate(facts, 1):
            print(f"{i}. {fact}")

if __name__ == "__main__":
    # Example usage: add a new fact and show all facts
    add_fact_to_archive()
    show_all_facts()
