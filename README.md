<div align=center>
  <h1>S.D.D - Subdomain Discovery</h1>
  <p>A basic subdomain enumeration tool.</p>
  <img src="https://img.shields.io/badge/Python-3.14-blue"/>
  <img src="https://img.shields.io/badge/CLI-Yes-orange"/>
  <img src="https://img.shields.io/badge/Version-1.0-green"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen"/>
  <img src="https://img.shields.io/badge/License-MIT-blue"/>
  </br>
</div>

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
> _This tool was created for training and study purposes in Python and is not intended for professional use. Feel free to contribute._
