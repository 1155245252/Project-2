# Digital Fact Collector

This project demonstrates how to use Python to connect to an open-source API and retrieve a random fact from the internet.

## What does it do?
- Connects to the [uselessfacts.jsph.pl](https://uselessfacts.jsph.pl/) API
- Fetches a random fact in English
- Prints the fact to your console

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

3. **See the result**
   
   The script will print a random fact to your console.

## What is happening?
- The script sends a request to the API.
- It receives a random fact in JSON format.
- The fact is extracted and displayed.

## Troubleshooting
- If you see an error about `requests` not being found, make sure you installed it with `pip install requests`.
- If you have network issues, check your internet connection.

---

This project is a simple example of how digital tools can interact with online data sources.
