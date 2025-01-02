import socket
import requests
import logging
import argparse

# Configure logging
logging.basicConfig(
    filename='net_connections.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def setup_argparse():
    parser = argparse.ArgumentParser(
        description="Track and log network connections - Basic network operations"
    )
    parser.add_argument(
        '--check-host', type=str, help='Check if a host is reachable (e.g., google.com)'
    )
    parser.add_argument(
        '--get-ip', type=str, help='Get the IP address of a hostname (e.g., google.com)'
    )
    parser.add_argument(
        '--test-url', type=str, help='Test if a URL is reachable (e.g., https://google.com)'
    )
    return parser

def check_host_reachable(hostname):
    try:
        logging.info(f"Checking if host '{hostname}' is reachable...")
        socket.gethostbyname(hostname)
        logging.info(f"Host '{hostname}' is reachable.")
        return f"Host '{hostname}' is reachable."
    except socket.error as e:
        logging.error(f"Host '{hostname}' is not reachable: {e}")
        return f"Host '{hostname}' is not reachable: {e}"

def get_ip_address(hostname):
    try:
        logging.info(f"Resolving IP for hostname '{hostname}'...")
        ip_address = socket.gethostbyname(hostname)
        logging.info(f"Hostname '{hostname}' resolved to IP '{ip_address}'.")
        return ip_address
    except socket.error as e:
        logging.error(f"Failed to resolve IP for hostname '{hostname}': {e}")
        return f"Error: {e}"

def test_url_reachability(url):
    try:
        logging.info(f"Testing URL reachability for '{url}'...")
        response = requests.get(url, timeout=5)
        logging.info(f"URL '{url}' is reachable with status code {response.status_code}.")
        return f"URL '{url}' is reachable with status code {response.status_code}."
    except requests.RequestException as e:
        logging.error(f"URL '{url}' is not reachable: {e}")
        return f"URL '{url}' is not reachable: {e}"

def main():
    parser = setup_argparse()
    args = parser.parse_args()

    if args.check_host:
        result = check_host_reachable(args.check_host)
        print(result)
    elif args.get_ip:
        result = get_ip_address(args.get_ip)
        print(f"IP Address: {result}")
    elif args.test_url:
        result = test_url_reachability(args.test_url)
        print(result)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()