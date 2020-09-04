# Project 1: Whois Service

[goto root](../README.md)

This project illustrates network communication to a server, which provides data about internet host domains.

Our task is to create an interactive client application, which can send request to one of the publicly known whois servers, for example `whois.dk-hostmaster.dk` or `internic.net`, and to print out the received response. The whois servers use port `43` for TCP communication with the clients.

_[extended information](https://datsoftlyngby.github.io/soft2020fall/resources/3eefb230-P1-WhoisClient.html)_

### Objectives
- [x] The server name and the communication port number - as arguments to the application
- [ ] Domain name of interest - at prompt
- [x] Outputs the domain data package, stored on the whois server

### General
This script uses the python libraries `sys` and `subprocess`.

The `sys` library handles extended input arguments on user execution.  
The `subprocess` library handles execution of `bash` commands.

By using `subprocess` within the script, error handling and functionality can be customized.

### Source
[main.py](./main.py)

### Execution

##### Main
This script takes 2 arguments `host`, `port`

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