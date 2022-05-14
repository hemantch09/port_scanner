import socket
import re
ip_add_pattern=re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_range_pattern=re.compile("([0-9]+)-([0-9]+)")
port_min =0
port_max =65535
open_ports = []
while True:
    ip_add_entered = input("Please enter valid ipv4 address = ")
    if ip_add_pattern.search(ip_add_entered):
        print(f"{ip_add_entered} is a valid ip address")
        break
    else:
        print(f"{ip_add_entered} is an invalid ip address")
        continue
while True:
    port_range = input("Enter port range = ")
    port_range_valid = port_range_pattern.search(port_range)
    if port_range_valid:
        port_min=int(port_range_valid.group(1))
        port_max=int(port_range_valid.group(2))
        break
for port in range(port_min, port_max+1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            s.connect((ip_add_entered,port))
            open_ports.append(port)
    except:
        pass

for port in open_ports:
    print(f"{port} is open on {ip_add_entered}")
