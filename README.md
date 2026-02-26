# S.D.D - Subdomain-Discovery
A basic subdomain enumeration tool.

## Usage
```sdd.py -h```
Show instructions for the tool usage.
```
sdd.py <https://taget_url> [wordlist_path] [optional]

~ sdd.py https://test.com wordlist.txt

Positional Arguments:
  url                   target url
  wordlist              wordlist path

Options:
  -h, --help            Show this help message and exit
  -T, --timeout         Set the timeout value (default = 5)          
  -V, --verbose         Verbosity mode (default = false)
```
