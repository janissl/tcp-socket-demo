#!/usr/bin/env python3

import sys
from datetime import datetime
import socket
import threading


mutex = threading.Lock()


class ClientThread(threading.Thread):
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn

    def run(self):
        with mutex:
            client_thread(self.conn)


def client_thread(conn):
    while True:
        received_data = conn.recv(1024).decode()

        if not (received_data and received_data.startswith('Time? ')):
            break
            
        client_id = received_data.split()[-1]
        data_to_send = '({}): {}'.format(client_id, datetime.now().isoformat(' '))
        conn.send(data_to_send.encode())

        print('Server response: {}'.format(data_to_send))

    conn.close()


def main():
    host = None
    port = 50007
    sck = None

    for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
        address_family, socket_type, protocol, canon_name, socket_address = res

        try:
            sck = socket.socket(address_family, socket_type, protocol)
        except OSError:
            sck = None
            continue

        try:
            sck.bind(socket_address)
            sck.listen()
        except OSError:
            sck.close()
            sck = None
            continue

        break

    if sck is None:
        sys.stderr.write('Cannot open the socket!\n')
        return 1

    while True:
        try:
            conn, addr = sck.accept()
        except Exception as ex:
            sys.stderr.write('Server terminated: {}\n'.format(repr(ex)))
            break

        c_thread = ClientThread(conn)
        c_thread.start()

    sck.close()


if __name__ == '__main__':
    sys.exit(main())
