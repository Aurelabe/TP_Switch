#!/usr/bin/env python3
import socket, argparse
from concurrent.futures import ThreadPoolExecutor

target = "192.168.189.201"

def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        r = s.connect_ex((ip, port))
        s.close()
        if r == 0:
            try: svc = socket.getservbyport(port)
            except: svc = "?"
            return port, svc
    except: pass
    return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", default=target)
    parser.add_argument("-p", "--ports", default="1-1024")
    args = parser.parse_args()
    
    if "-" in args.ports:
        start, end = map(int, args.ports.split("-"))
        ports = range(start, end+1)
    else:
        ports = [int(p) for p in args.ports.split(",")]
    
    print(f"Scanning {args.target}...")
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as ex:
        results = ex.map(lambda p: scan_port(args.target, p), ports)
        for r in results:
            if r:
                open_ports.append(r)
                print(f"  OPEN: {r[0]} ({r[1]})")
    print(f"Done. Found {len(open_ports)} open ports")

if __name__ == "__main__":
    main()
