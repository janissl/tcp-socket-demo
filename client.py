#!/usr/bin/env python3

import os
import sys
import socket


def main(host='localhost'):
    port = 50007

    max_calls = 10000
    counter = 0
    client_id = str(os.getpid())

    while counter < max_calls:
        counter += 1
        sck = None

        for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM):
            address_family, socket_type, protocol, canon_name, socket_address = res

            try:
                sck = socket.socket(address_family, socket_type, protocol)
            except OSError:
                sck = None
                continue

            try:
                sck.connect(socket_address)
            except OSError:
                sck.close()
                sck = None
                continue

            break

        if sck is None:
            sys.stderr.write('Cannot open the socket!\n')
            return 1

        with sck:
            sck.sendall('Time? {}'.format(client_id).encode())

            try:
                response = sck.recv(1024)
            except ConnectionError as ex:
                sys.stderr.write('{}\n'.format(ex.strerror))
                sys.exit(1)

        print('Current time: {}'.format(response.decode()))


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
