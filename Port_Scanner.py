import argparse
import socket

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
args = parser.parse_args()

def scan(target, ports, verbose):
    for port in range (1, ports):
        scan_port(target, port, verbose)

def scan_port(ipaddress, port, verbose):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f"[+] Port {port} is open")
        open_ports.append(port)
    except:
        if verbose:
            print(f"[-] Port {port} is closed")

def end (verbose):
    if verbose:
        print("----------------------------------")
        print(f"[*] Out of {ports} ports, {len(open_ports)} were open")
        print(f"[*] The ports {open_ports} are all open.")
    else:
        pass

targets = input("[*] Enter targets to scan (Split them by comma): ")
ports = int(input("[*] Enter how many ports you want to scan: "))

open_ports = []
ip_list = targets.split(',')

if ',' in targets:
    print("----------------------------------")
    print(f"[*] Scanning multiple targets - {ip_list[0:]}")
    print("----------------------------------")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports, args.verbose)
else:
    print("----------------------------------")
    print(f"[*] Scanning {targets}")
    print("----------------------------------")
    scan(targets, ports, args.verbose)

end(args.verbose)
