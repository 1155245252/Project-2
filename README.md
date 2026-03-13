# Digital Fact Collector

This project demonstrates how to use Python to connect to an open-source API, retrieve a random fact, and build a persistent local archive of unique facts.

## What does it do?
- Connects to the [uselessfacts.jsph.pl](https://uselessfacts.jsph.pl/) API
- Fetches a random fact in English
- Stores unique facts in a local `facts.json` file (prevents duplicates)
- Lets you view your growing archive of facts

## How to use

1. **Install dependencies**
   
   This script requires the `requests` library. If you don't have it, install it with:
   
   ```bash
   pip install requests
   ```

2. **Run the script**
   
   Open a terminal in this folder and run:
   
   ```bash
   python "digital fact collector.py"
   ```

3. **What happens?**
   - The script fetches a random fact from the API.
   - If the fact is not already in your archive, it is added to `facts.json`.
   - If the fact is already present, it is not added again.
   - All facts in your archive are displayed in the console.

## Storage Format
- Facts are stored in a local file called `facts.json` as a list of strings (one per fact).
- The script checks for duplicates (case-insensitive) before adding new facts.

## Troubleshooting
- If you see an error about `requests` not being found, make sure you installed it with `pip install requests`.
- If you have network issues, check your internet connection.
- If `facts.json` is missing or empty, it will be created automatically.

---

This project is a simple example of how digital tools can interact with online data sources and build a persistent knowledge base.

---

This project is a simple example of how digital tools can interact with online data sources.
