# Osintinel

This tool is designed to perform Open Source Intelligence (OSINT) gathering from various sources, similar to Spiderfoot. It will be a command-line interface (CLI) tool written in Python.

## Project Structure

- `src/`: Main source code directory
  - `modules/`: Individual modules for different OSINT sources
  - `cli/`: Command line interface components
- `data/`: Directory for storing retrieved data
- `reports/`: Directory for storing generated reports
- `requirements.txt`: Python dependencies
- `.gitignore`: Git ignore file
- `README.md`: Project documentation

## Getting Started

### Prerequisites

- Python 3.x
- Virtual environment setup

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/bitterbuick/osintinel.git
    cd osintinel
    ```

2. Set up the virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

    Only `requests`, `beautifulsoup4` and `python-dotenv` are required. The rest
    are optional and each is needed by exactly one command — the CLI runs
    without them and tells you what to install if you reach for one.

### Usage

Each OSINT source is a subcommand:

```bash
python src/cli/cli.py --help              # list every command
python src/cli/cli.py dns example.com     # resolve a domain
python src/cli/cli.py geo 8.8.8.8         # geolocate an IP (ipinfo.io)
python src/cli/cli.py emails https://example.com   # scrape addresses off a page
python src/cli/cli.py github octocat      # public GitHub profile
python src/cli/cli.py github octocat --repos       # their public repositories
```

These five need no credentials and no API keys.

| Command | Extra package | Credentials |
|---|---|---|
| `dns`, `geo`, `emails`, `github` | — | none |
| `whois` | `python-whois` | none |
| `darkweb` | — | a Tor SOCKS proxy on `127.0.0.1:9050` |
| `twitter` | `tweepy` | `TWITTER_*` in `.env` |
| `linkedin` | `linkedin-api` | `LINKEDIN_*` in `.env` |

Credentials are read from a `.env` file in the repository root (see `src/config.py`
for the variable names). Output is printed to stdout; `data/` and `reports/` are
there for anything you choose to redirect into them.

### Running the tests

```bash
python -m unittest discover tests
```


## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

