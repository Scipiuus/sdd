# S.D.D - Subdomain-Discovery
A basic subdomain enumeration tool.

## Installation
```
git clone https://github.com/Scipiuus/SDD.git
```
S.D.D currently supports Python 3.2+

### Dependencies
To run properly, S.D.D depends on the following modules:
  - `requests`
  - `tldextract`
    
Also, it requires a subdomain `wordlist`. The supported files extension are: `".txt"` and `".list"`.

#### Requirements installation:
* Windows:
```
c:/python32/python.exe -m pip install requirements.txt
```

* Linux:
```
sudo pip install -r requirements.txt
```

## Usage
```
sdd.py -h
```
Show instructions for the tool usage.

```
sdd.py <https://taget_url> [wordlist_path] [option]

~ sdd.py https://test.com wordlist.txt -V -T2

Positional Arguments:
  url                   target url
  wordlist              wordlist path

Options:
  -h, --help            Show this help message and exit
  -T, --timeout         Set the timeout value (default = 5)          
  -V, --verbose         Verbosity mode (default = false)
```

### Usage Example
```
python sdd.py https://www.google.com usr/wordlists/sublist.txt -V -T5
```
# License
S.D.D is licensed under the GNU GPL license. take a look at the [LICENSE](LICENSE.md) for more information.

> [!NOTE]
> Useful information that users should know, even when skimming content.
