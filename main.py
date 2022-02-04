from concurrent.futures import thread
from resolver import Resolver
import ipaddress
from threading import Thread

IP = ipaddress.IPv4Address('1.1.1.1')

def check(dns):
    r = Resolver(dns)
    if r.is_vulnerable():
        return True
    else:
        return False


def next():
    global IP
    IP+=1
    return str(IP)

def start():
    while str(IP) != '255.255.255.255':
        v = check(next())
        print(f"{str(IP)} = {v}")
        if v:
            open('result.txt', 'a+').write(str(IP) + "\nb")

if __name__ == "__main__":    
    start()
