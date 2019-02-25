import socket
import sys
"""
Python script for port scanning.
"""
def scan_port(port, ip, sock):
    """Scan certain port by ip and socket.
    Return True if port is open and False if note.
    """
    try:
        if sock.connect_ex((ip, port)) == 0:
            return True
    except Exception as exc:
        print("port_scan function Exception: ", exc)
        return False

def get_socket():
    """Socket creating.
    Return socket or None if socket opening is not possible.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return sock
    except Exception as exc:
        print("create_socket function Exception: ", exc)
        return None

def get_ip(host, sock):
    """Get ip or None if getting ip is not possible."""
    try:
        return socket.gethostbyname(host)
    except Exception as exc:
        print("get_ip function Exception: ", exc)
        return None

def scan_in_range(from_port, to_port, ip, sock):
    """Scanning ports in defined range."""
    for port in range(from_port, to_port):
        if scan_port(port, ip, sock):
            print(port, "OPEN")

def main():
    host = input("Host name: ")
    sock = get_socket()
    ip = get_ip(host, sock)
    scan_in_range(1, 1000, ip, sock)

main()
