# Project 1: Whois Service

### Objectives
- [x] The server name and the communication port number - as arguments to the application
- [ ] Domain name of interest - at prompt
- [x] Outputs the domain data package, stored on the whois server

_[extended objectives](https://datsoftlyngby.github.io/soft2020fall/resources/3eefb230-P1-WhoisClient.html)_


### General
This script uses the python libraries `sys` and `subprocess`.

The `sys` library handles extended input arguments on user execution.  
The `subprocess` library handles execution of `bash` commands.

By using `subprocess` within the script, error handling and functionality can be customized.

### Source
[main.py](./main.py)

### Execution

This script takes two arguments [`host`, `port`]

Structure
```bash
python main.py <host> <port>
```

Example
```bash
python main.py http://whois.arin.net/ 43
```

#### Conditions

| On | Description |
| --- | --- |
| - no `host` provided | The script will use a fallback host `whois.dk-hostmaster.dk` |
| - no `port` provided | The script will use a fallback port `43` |

#### Exceptions

| On | Message |
| --- | --- |
| - empty response | Couldn't find host `<host>` |
| - response code 68 | Couldn't get connection to `<host>` |
| - default error | Unknown error while connecting to `<host>` |