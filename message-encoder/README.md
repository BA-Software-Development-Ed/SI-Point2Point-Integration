# Project 2: Message Encoder

### Objectives
- [ ] Server opens one of its ports, preferably with a number > 1024, for example 6666, and creates a socket for it
- [ ] Server declares that is ready to listen and accept requests
- [ ] If a message from a Client comes on this port, Server processes it, by reverting the text.
- [ ] Server keeps listening, until a `stop` command comes from the Client

_[extended objectives](https://datsoftlyngby.github.io/soft2020fall/resources/ec16b918-P2-TCP.html)_

### General


### Source
[server.py](./server.py)
[client.py](./client.py)

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