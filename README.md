# Digital Fact Collector

This project demonstrates how to use Python to connect to an open-source API, retrieve a random fact, and build a persistent local archive of unique facts—automatically and continuously.

## What does it do?
- Connects to the [uselessfacts.jsph.pl](https://uselessfacts.jsph.pl/) API
- Fetches a random fact in English
- Stores unique facts in a local `facts.json` file (prevents duplicates)
- Periodically fetches and archives new facts automatically (no manual intervention needed)
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

   By default, the script will fetch a new fact every 60 seconds and add it to your archive if it's unique. It will keep running until you stop it (press Ctrl+C in the terminal).

   You can adjust the fetch interval or set a maximum number of fetches by editing the `auto_collect_facts` call at the bottom of the script.

3. **Automate on a schedule (optional)**
   - The script only runs when you execute it manually.
   - To have it start automatically on a schedule, use Windows Task Scheduler, a cron job (Linux/macOS), or a Python scheduler library.
   - For most users, simply running the script and letting it run in the background is sufficient.

## What happens?
- The script fetches a random fact from the API at regular intervals.
- If the fact is not already in your archive, it is added to `facts.json`.
- If the fact is already present, it is not added again.
- All facts in your archive are displayed if you use the `show_all_facts()` function.

## Storage Format
- Facts are stored in a local file called `facts.json` as a list of strings (one per fact).
- The script checks for duplicates (case-insensitive) before adding new facts.

## Troubleshooting
- If you see an error about `requests` not being found, make sure you installed it with `pip install requests`.
- If you have network issues, check your internet connection.
- If `facts.json` is missing or empty, it will be created automatically.

---

This project is a simple example of how digital tools can interact with online data sources and build a persistent, automatically growing knowledge base.

---

This project is a simple example of how digital tools can interact with online data sources.
