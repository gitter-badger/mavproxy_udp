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
