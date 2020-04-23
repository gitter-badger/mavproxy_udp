
[![Join the chat at https://gitter.im/mavproxy_udp/community](https://badges.gitter.im/mavproxy_udp/community.svg)](https://gitter.im/mavproxy_udp/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

MAVProxy_udp:

usage: mavproxy_udp.py [-h] [--in_port IN_PORT] [--out_port OUT_PORT]
                       [--dest_addr DEST_ADDR]

Commands for creating a proxy between udp ports

optional arguments:
  -h, --help            show this help message and exit
  --in_port IN_PORT     Input UDP port (default = 14550)
  --out_port OUT_PORT   Initial UDP output port (Other UDP ports start from
                        this UDP port with the incremental of 1) (default =
                        1220)
  --dest_addr DEST_ADDR
                        Destination address for message forwarding (default =
                        '')
