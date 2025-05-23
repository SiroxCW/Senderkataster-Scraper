
# Senderkataster Scraper

A Python script to fetch and save detailed sender data from [senderkataster.at](https://www.senderkataster.at/). The script retrieves all sender entries, fetches their details, and periodically saves the results to a JSON file.

## Features

- Fetches all sender entries from the Senderkataster API.
- Retrieves detailed information for each sender.
- Saves senders and all of its details to `senderkataster.json`.
- Logs progress and errors.

## Requirements

- Python 3.7+
- `requests` library

## Installation

```bash
pip install requests
```

## Usage

Run the script:

```bash
python scraper.py
```

The script will create or update `senderkataster.json` in the current directory.

## Output

- `senderkataster.json`: Contains all sender data with detailed information.

## License

MIT License

