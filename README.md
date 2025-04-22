# DDOS Toolkit

**DDOS Toolkit** is a network stress testing and load simulation tool designed for research, audit, and penetration testing purposes only.

### Features

- Layer 4: UDP and TCP packet flooding
- Layer 7: HTTP GET/POST simulation
- Proxy rotation (SOCKS5/HTTP)
- Multithreaded engine
- CLI-based control

> Warning: This tool is meant for educational and authorized testing only.

### Usage

```bash
python runner.py --mode http --target https://your.test.site --threads 200 --duration 60 --proxy proxies/socks5.txt
