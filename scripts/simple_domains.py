# Simple subdomain scanner

import os
import requests
import concurrent.futures
from colorama import Fore, Style
import urllib.request

# List of domains (can be customized)
SUBDOMAINS = [
    'www', 'mail', 'ftp', 'webmail', 'localhost', 'cpanel', 'api', 'test', 'dev'
]

# Utilities
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Verify online status
def is_online(host, timeout):
  try:
      urllib.request.urlopen(host, timeout=timeout)
      return True
  except:
      print(Fore.YELLOW + "Warning⚠️ : You are not connected to internet!")


# Verify valid subdomains
def check_subdomain(domain, subdomain):
  url = f"http://{subdomain}.{domain}"
  try:
    response = requests.get(url, timeout=3)
    if response.status_code < 400:
      print(f"{Fore.GREEN}[+] {url} -> {response.status_code}{Style.RESET_ALL}")
      return url
  except requests.ConnectionError:
    pass
  except requests.Timeout:
    pass
  return None

# Scan subdomains
def scan(domain, threads=10):
    found = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(check_subdomain, domain, sub) for sub in SUBDOMAINS]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                found.append(result)
    return found

# Main menu for simple scanning
def simple_scan_menu():
    while True:
        clear()
        print(Fore.LIGHTMAGENTA_EX + "Domains list: ", end="")
        for subdomain in SUBDOMAINS:
            print(Fore.LIGHTMAGENTA_EX + f"{subdomain}", end=", ")

        print("\n")
        target = input(Fore.RED + "Target: ")

        print(f"{Fore.CYAN}[*] Scanning domain: {target}{Style.RESET_ALL}")
        results = scan(target, 10)

        print(f"\n{Fore.LIGHTBLUE_EX}[!] Found {len(results)} valid subdomains:{Style.RESET_ALL}")
        for r in results:
            print(f" - {r}")

        # Verify online status
        is_online('http://www.google.com',3)

        # Again loop
        choice = input(Fore.YELLOW + "\n¿New Scan? (y/n): ").lower()
        if choice != 'y':
            clear()
            break
