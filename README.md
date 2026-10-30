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
python main.py --check-host <hostname>
python main.py --get-ip <hostname>
python main.py --test-url <url>
```

where:

* **--check-host HOSTNAME** prints whether the hostname resolves to an IP address
* **--get-ip HOSTNAME** prints the IP address the hostname resolves to
* **--test-url URL** prints whether the URL is reachable and its HTTP status code
* **-h** displays the help message

With no option given, the script prints its help text. For example, to print the IP address of a hostname:

```
python main.py --get-ip example.com
```

## Security Warnings

net-connections only performs the three checks above: it does not open or track connections to a host and port, and it does not send or receive application data.

## License

net-connections is licensed under the GNU General Public License v3.0. This license allows you to use, modify, and distribute the software for free. The software is licensed to CY83R-3X71NC710N.