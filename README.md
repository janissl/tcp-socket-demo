# tcp-socket-demo
A demo application to demonstrate a client-server communication using TCP sockets


The client part sends a message 'Time?' (i.e. 'What's the time?') and the server part responds to this message by sending the current time string in an ISO 8601 format using a space as a date/time separator. The server part has been implemented in two versions - a single-threaded and a multi-threaded. Both the client and the server use port 50007 for the communication.

The application has been developed in course of my master studies at [Riga Technical University] (Network Operating Systems (DIP 496), Prof. Dr. E. Latiseva).

## Usage
### 1. First, start a server.
__UNIX/Linux__ _(single-threaded)_:
```
$>./server_sgl_conn.py
```  
__OR__ _(multi-threaded)_:
```
$>./server_mtp_conn.py
```
__Windows__ _(from PowerShell console, single-threaded)_:
```
$>python .\server_sgl_conn.py
```
__OR__ _(multi-threaded)_:
```
$>python .\server_mtp_conn.py
```
### 2. Then, run the client.
__UNIX/Linux__:
```
$>./client.py [server_IP_address]
```
__Windows__ _(from PowerShell console)_:
```
$>python .\client.py [server_IP_address]
```

If the client and the server are running on the same machine, the server IP address may be omitted.
<hr>

Used references:
* [19.1. socket — Low-level networking interface]
* [Python network sockets programming tutorial]
* [How to Work with TCP Sockets in Python (with Select Example)]
* [Socket Programming with Multi-threading in Python]

[Riga Technical University]: https://www.rtu.lv/
[19.1. socket — Low-level networking interface]: https://docs.python.org/3/library/socket.html
[Python network sockets programming tutorial]: https://pythonspot.com/python-network-sockets-programming-tutorial/
[How to Work with TCP Sockets in Python (with Select Example)]: https://steelkiwi.com/blog/working-tcp-sockets/
[Socket Programming with Multi-threading in Python]: https://www.geeksforgeeks.org/socket-programming-multi-threading-python/
