import os
import socket
from pathlib import Path

from distlib.compat import raw_input
from requests import get

def clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])
def existIpFile():
    path_to_file = 'ip.txt'
    path = Path(path_to_file)
    if path.is_file():
        os.remove(path_to_file)
    else:
        file = open("ip.txt", "w")
        file.close()

def isOpen(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect((ip, int(port)))
        s.shutdown(socket.SHUT_RDWR)
        file = open("ip.txt", "a+")
        file.write(ip + " ")
        print(" " + ip + ":" + port, "Is up")
    except:
        print(" " + ip + ":" + port, "Is Down")
    finally:
        s.close()
def ipRange(start_ip, end_ip):
    start = list(map(int, start_ip.split(".")))
    end = list(map(int, end_ip.split(".")))
    temp = start
    ip_range = []

    ip_range.append(start_ip)
    while temp != end:
        start[3] += 1
        for i in (3, 2, 1):
            if temp[i] == 256:
                temp[i] = 0
                temp[i - 1] += 1
        ip_range.append(".".join(map(str, temp)))

    return ip_range
    pass

Exteral_IP = get('https://api.ipify.org').text
From = raw_input(" Put Start Ip => ")
To = raw_input(" Put End Ip   => ")
ip_range = ipRange(From, To)
port = raw_input(" Put Port To Check  in If It is Up => ")
print(" Starting scanner From", From, "To", To)
print(" Your External Ip ", Exteral_IP)
existIpFile()
for ip in ip_range:
    isOpen(ip, port)
