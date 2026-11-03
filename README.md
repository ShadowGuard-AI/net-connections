![Banner](banner.png)

# net-connections

## Project Description

net-connections is a small network utility with three checks, implemented in the single script `main.py`: it reports whether a hostname resolves, prints the IP address a hostname resolves to, and reports whether a URL answers an HTTP request (with its status code). Every check is also written to a log file named `net_connections.log` in the working directory.

## Installation

The tool is a single script (`main.py`) and is not published as a pip package. Clone this repository, then install its one third-party dependency, requests (everything else it imports is in the Python standard library; the repo ships no requirements.txt):

```
pip install requests
```

## Usage Examples

Run the script with exactly one of its three options:

```
python3 main.py --check-host <hostname>
python3 main.py --get-ip <hostname>
python3 main.py --test-url <url>
```

where:

* **--check-host HOSTNAME** prints whether the hostname resolves to an IP address
* **--get-ip HOSTNAME** prints the IP address the hostname resolves to
* **--test-url URL** prints whether the URL is reachable and its HTTP status code
* **-h** displays the help message

With no option given, the script prints its help text. For example, to print the IP address of a hostname:

```
python3 main.py --get-ip example.com
```

## Security Warnings

net-connections only performs the three checks above: it does not open or track connections to a host and port, and it does not send or receive application data.

## Notes verified in Wave 12

- Only the first flag given runs, in this order: `--check-host`, then `--get-ip`, then `--test-url`. Extra flags are parsed and silently ignored, not combined.
- `--check-host` reachable means only that the name resolves in DNS; no connection is opened, so a host that answers DNS but refuses every port still reports as reachable.
- `--test-url` reachable means a server answered with any HTTP status, including 404 or 500; it does not mean the page is healthy.
- `--get-ip` on a name that does not resolve prints the error text after an "IP Address:" label, with no separate failure signal.
- Every run writes `net_connections.log` in the working directory, and even a `--help` run creates that file, because the log handler opens at import time.

## License

GNU General Public License v3.0. See [LICENSE](LICENSE).