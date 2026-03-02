<div align=center>
<pre>
   █████████     ██████████      ██████████  
  ███░░░░░███   ░░███░░░░███    ░░███░░░░███ 
 ░███    ░░░     ░███   ░░███    ░███   ░░███
 ░░█████████     ░███    ░███    ░███    ░███
  ░░░░░░░░███    ░███    ░███    ░███    ░███
  ███    ░███    ░███    ███     ░███    ███ 
 ░░█████████  ██ ██████████   ██ ██████████  
  ░░░░░░░░░  ░░ ░░░░░░░░░░   ░░ ░░░░░░░░░░   
</pre>
  <h1>S.D.D - Subdomain Discovery</h1>
  <p>A basic subdomain enumeration tool.</p>
  <img src="https://img.shields.io/badge/Python-3.14-blue"/>
  <img src="https://img.shields.io/badge/CLI-Yes-orange"/>
  <img src="https://img.shields.io/badge/Version-1.0-green"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen"/>
  <a href="https://github.com/Scipiuus/sdd/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-GNU-blue"/></a>
  </br>
</div>

## Installation
```
git clone https://github.com/Scipiuus/sdd.git
```
S.D.D currently supports Python 3.10+

### Dependencies
To run properly, S.D.D depends on the following modules:
  - `requests`
  - `tldextract`
    
Additionally, it requires a subdomain `wordlist`. The supported files extension are: `".txt"` and `".list"`.

#### Requirements Installation:
* Windows:
```
py -m pip install -r requirements.txt
```

* Linux:
```
$ pip install -r requirements.txt
```

## Usage
```
$ python sdd.py -h
```
Displays instructions for using the tool.

```
sdd.py <https://taget_url> [wordlist_path] [option]

$ sdd.py https://test.com wordlist.txt -V -T2

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
$ python sdd.py https://www.google.com usr/wordlists/sublist.txt -V -T5
```
If the verbosity is activated the script will return every domain tested and the status code, else, the script will not show the tests, but a list of the sucessfull tests will be printed in the end.


# License
S.D.D is licensed under the GNU General Public License. take a look at the [LICENSE](LICENSE) for more information.

> [!NOTE]
> _This tool was created for training and study purposes in Python and is not intended for professional use. Feel free to contribute and suggest any improvement._
