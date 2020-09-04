# Project 3: Capital Echo

This project illustrates control over the communication and exchange of text messages between a client and a server over UDP protocol.

The client sends a text message to the server, and the server returns it back, after processing.

_[extended information](https://datsoftlyngby.github.io/soft2020fall/resources/f72fb747-P3-UDP.html)_

### Objectives
- [x] The client sends a text message to the server, and the server returns it back, after processing.
- [x] The processing protocol enables simple echoing after capitalization of the message letters.
- [ ] Instead, the server extracts the IP address of the client, every time it gets request.

#### Homework Task
UDP protocol provides faster transmission of messages, and therefore is a preferable for transmitting large, binary and video-streaming data.

- [ ] Modify the program above, so it can be applied for sending and receiving image data from a binary file.

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

This script takes 1 argument `host`, `port` and `message`

Structure
```bash
python client.py <host> <port> <message>
```

Example
```bash
python client.py 127.0.0.1 20001 "Hello CPHBusiness"
```

#### Conditions

| On | Description |
| --- | --- |
| - no `host` provided | The script will use a fallback host `127.0.0.1` |
| - no `port` provided | The script will use a fallback port `20001` |
| - no `message` provided | The script will use a fallback message `default message` |

#### Exceptions

| On | Message |
| --- | --- |
| - request failure | Couldn't get connection to `<host>` |