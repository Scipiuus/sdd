#CREATED BY SCIPIUUS - https://github.com/Scipiuus
#PROJECT S.D.D - Subdomain Discover
#DESC: This is a simple and basic tool made for subdomain enumeration.
#VERSION: 1.0

import sys
import socket
import requests
import argparse

import tldextract
from urllib.parse import urlparse

def print_header():
    banner = """
#   █████████     ██████████      ██████████  
#  ███░░░░░███   ░░███░░░░███    ░░███░░░░███ 
# ░███    ░░░     ░███   ░░███    ░███   ░░███
# ░░█████████     ░███    ░███    ░███    ░███
#  ░░░░░░░░███    ░███    ░███    ░███    ░███
#  ███    ░███    ░███    ███     ░███    ███ 
# ░░█████████  ██ ██████████   ██ ██████████  
#  ░░░░░░░░░  ░░ ░░░░░░░░░░   ░░ ░░░░░░░░░░   
"""
    print(banner)
    print('\033[90m#[PROJECT]:\033[0m S.D.D — Subdomain Discovery')
    print('\033[90m#[AUTHOR]:\033[0m scipiuus')
    print('\033[90m#[VERSION]:\033[0m v1.0')
    print('\033[90m#[GITHUB]:\033[0m https://github.com/Scipiuus/sdd')
    print('\033[90m# # # # # # # # # # # # # # # # # # # # # # # # # # # # #\033[0m')


def print_input_info(input_url, input_wordlist):
    print('===============================================')
    print(f'\033[96m[TARGET]: \033[0m{input_url}')
    print(f'\033[96m[WORDLIST]: \033[0m{input_wordlist}')
    print('===============================================')


def create_parser():
    parser = argparse.ArgumentParser( 
        prog='sdd.py',
        usage='sdd.py <https://taget_url> [wordlist_path] [optional]',
        description='~ sdd.py https://test.com wordlist.txt'
    )
    
    parser.add_argument(
        'url', 
        type=str, 
        help='target url')
    
    parser.add_argument(
        'wordlist', 
        type=str, 
        help='wordlist path')
    
    parser.add_argument(
        '-T',
        '--timeout',
        type=float, 
        default=5, 
        help='set the timeout value (default = 5)')
    
    parser.add_argument(
        '-V',
        '--verbose',
        action='store_true', 
        default=False, 
        help='verbosity mode (default = false)')

    if (len(sys.argv) == 1):
        raise ValueError('Missing required arguments. Type "-help" for instructions.\n')
    
    else:
        return parser


def validate_base_domain(base_url):
    url_parse = urlparse(base_url)
    try:
        if url_parse.scheme in base_url:
            base_url = base_url.replace(url_parse.scheme + '://', '')
            socket.gethostbyname(base_url)

        return True
    
    except Exception as e:
        raise ValueError('Invalid URL.')
    
def validate_domain(verbose, domain, timeout):
    try:
        response = requests.head(domain, timeout=timeout, allow_redirects=True)
        status_code = str(response.status_code)

        if verbose:
            if response.ok:
                print(f'\033[32m[ACTIVE]\033[0m {domain} -> \033[92m[{status_code}\033[0m]')

            else:
                print(f'\033[33m[UNAVAILABLE]\033[0m {domain} -> \033[33m[{status_code}\033[0m]')
                
        return True
    
    except requests.exceptions.InvalidURL:
        raise ValueError('Invalid target.\n')

    except requests.exceptions.Timeout:
        if verbose:
            print(f'\033[31m[FAILED]\033[0m {domain} \033[31m[TIMED OUT]\033[0m')

    except requests.exceptions.RequestException:
        if verbose:
            print(f'\033[31m[FAILED]\033[0m Failed to resolve {domain}')

    


def assemble_domains(url, wordlist):
    parsed_url = urlparse(url)
    url_extracted = tldextract.extract(url)

    scheme = parsed_url.scheme
    subdomain = url_extracted.subdomain
    domain = url_extracted.domain
    suffix = url_extracted.suffix

    if scheme not in ('http', 'https'):
        raise ValueError('Invalid URL scheme.\n')

    if not wordlist.lower().endswith(('.txt', '.list')):
        raise ValueError('Invalid file extension.\n')

    url_list = []
    try:
        with open(wordlist, 'r') as sublist:
            for subdomain in map(str.strip, sublist):
                if subdomain:
                    new_domain = f"{scheme}://{subdomain}.{domain}.{suffix}"
                    url_list.append(new_domain)
                     

    except FileNotFoundError:
        raise ValueError('Wordlist not found.')

    except IOError:
        raise ValueError('Failed reading wordlist.')
    
    return url_list


def main():
    try:
        print_header()
        
        parser = create_parser()
        args = parser.parse_args()
        print_input_info(args.url, args.wordlist)

        success_list = []
        if validate_base_domain(args.url):
            urls = assemble_domains(args.url, args.wordlist)

            for target in urls:
                if validate_domain(args.verbose, target, args.timeout):
                    success_list.append(target)
    
        if not args.verbose:
            print('\n\033[32m============ [ACTIVE DOMAINS LIST] ============ \033[0m')
            for item in success_list:
                print(f'\033[32m[+] {item}\033[0m')
    

    except Exception as e:
        print(f'\033[31m[ERROR]\033[0m {e}')
        return 1

if __name__ == '__main__':
    sys.exit(main())
