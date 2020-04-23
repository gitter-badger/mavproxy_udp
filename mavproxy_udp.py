#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
© Copyright 2020 - 2021, masoud-iranmehr.
mavproxy_udp.py: converts from one udp port to multi-udp ports (each connection gets its own new port)

Automatically forwards new udp connections to a new udp port.

Full documentation is provided at https://gitlab.com/masoud-iranmehr/mavlink_udp_proxy
"""
from __future__ import print_function

import socket
import time

# Set up option parsing to get config string
import argparse

parser = argparse.ArgumentParser(description='Commands for creating a proxy between udp ports')
parser.add_argument('--in_port', help="Input UDP port (default = 14550)")
parser.add_argument('--out_port',
                    help="Initial UDP output port (Other UDP ports start from this UDP port with the incremental of 1) (default = 1220)")
parser.add_argument('--dest_addr', help="Destination address for message forwarding (default = '')")
args = parser.parse_args()

in_port = args.in_port
out_port = args.out_port
dest_addr = args.dest_addr


class MavUdpProxy:
    def __init__(self):
        self.input_port = 14550
        self.output_port = 1220
        self.addr_list = []
        self.IP = ""
        self.PORT = self.input_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.IP, self.PORT))
        self.dest_addr = ""

    def get_port(self, addr):
        for i in range(len(self.addr_list)):
            if addr == self.addr_list[i]:
                return i + self.output_port
        self.addr_list.append(addr)
        new_port = len(self.addr_list) - 1 + self.output_port
        return new_port

    def receive(self, buff_size):
        data, addr = self.socket.recvfrom(buff_size)
        if addr and data:
            dest_port = self.get_port(addr)
            print(data, addr)
            print(dest_addr, dest_port)
            self.socket.sendto(data, (dest_addr, dest_port))


if __name__ == "__main__":
    sock = MavUdpProxy()
    if in_port is not None:
        sock.input_port = int(in_port)
    if out_port is not None:
        sock.output_port = int(out_port)
    if dest_addr is not None:
        sock.dest_addr = str(dest_addr)
    while True:
        sock.receive(1024)
