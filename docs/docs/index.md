# Welcome to MAVProxy_udp

For full documentation visit [masoud-iranmehr.github.io/mavproxy_udp/](https://masoud-iranmehr.github.io/mavproxy_udp/).

## Commands

* `mavproxy_udp.py -h` - Shows available commands for help.
* `mavproxy_udp.py --in_port [INPUT_PORT]` - Input UDP port (default = 14550).
* `mavproxy_udp.py --out_port [OUTPUT_PORT]` - Initial UDP output port (Other UDP ports start from this UDP port with the incremental of 1) (default = 1220).
* `mavproxy_udp.py --dest_addr [DESTINATION_ADDRESS]` - Destination address for message forwarding (default = '').

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
