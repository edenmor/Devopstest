import socket
import argparse

def main():
    ARGS = get_args()
    server_inspect(ARGS.dest).inspect_port(ARGS.start, ARGS.end)

if __name__ == "__main__":
    main()

print ("Hello world")