# Project 2: Message Encoder

[goto root](../README.md)

This project illustrates control over the communication and exchange of text messages between a client and a server using TCP protocol over Sockets and endpoints.

Server opens a server socket on a specified port and starts listening on it. When the socket detects an incoming connection, it will accept it and create a new `Socket` instance to facilitate the communication to the client, sending the request.

_[extended information](https://datsoftlyngby.github.io/soft2020fall/resources/ec16b918-P2-TCP.html)_

### Objectives
- [x] Server opens one of its ports, preferably with a number > `1024`, for example `6666`, and creates a socket for it
- [x] Server declares that is ready to listen and accept requests
- [x] If a message from a Client comes on this port, Server processes it, by reverting the text.
- [x] Server keeps listening, until a `stop` command comes from the Client

#### Homework Task
In the reality, servers often have to serve multiple clients at the same time.

- [x] Modify the program above, so then server would be able to listen to more than one clients in parralel, running multiple threads.

### General

### Source
[server.py](./server.py)
[client.py](./client.py)

### Execution

This solution uses two terminal instances.  
The first is for the server and the second is for the client.

##### Server

```bash
python server.py
```

##### Client

This script takes 3 arguments `host`, `port` and `payload`

Structure
```bash
python client.py <host> <port> <payload>
```

Example
```bash
python client.py http://127.0.0.1 6666 "Hello CPHBusiness"
```

_Set the payload to `stop` for terminating the server._ 

#### Conditions

| On | Description |
| --- | --- |
| - no `host` provided | The script will use a fallback host `http://127.0.0.1` |
| - no `port` provided | The script will use a fallback port `6666` |
| - no `payload` provided | The script will use a fallback port `default payload` |

#### Exceptions

| On | Message |
| --- | --- |
| - request failure | Couldn't get connection to `<host>` |