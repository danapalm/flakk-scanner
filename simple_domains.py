# Escáner de Subdomínios Simples

import requests
import concurrent.futures
import argparse
from colorama import Fore, Style

# Lista base de subdomínios comunes (se puede ampliar según sea necesario)
SUBDOMAINS = [
    'www', 'mail', 'ftp', 'webmail', 'localhost', 'cpanel', 'api', 'test', 'dev'
]

# Función para verificar si un subdominio es válido
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

# Función principal para escanear subdominios
def scan(domain, threads=10):
    found = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(check_subdomain, domain, sub) for sub in SUBDOMAINS]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                found.append(result)
    return found

def main():
    parser = argparse.ArgumentParser(description='Subdomain Scanner')
    parser.add_argument('domain', help='Target domain')
    parser.add_argument('--threads', type=int, default=10, help='Number of threads (default=10)')
    args = parser.parse_args()

    print(f"{Fore.CYAN}[*] Scanning domain: {args.domain}{Style.RESET_ALL}")
    results = scan(args.domain, args.threads)

    print(f"\n{Fore.LIGHTBLUE_EX}[!] Found {len(results)} valid subdomains:{Style.RESET_ALL}")
    for r in results:
        print(f" - {r}")

main()
