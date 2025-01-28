import socket

def scan_ports(ip, start_port, end_port):
    print("Scanning {}...".format(ip))
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((ip, port))  # prints 0 on success and nothing on failure
        if result == 0:
            print("[+] Port {} is open on {}".format(port, ip))
        s.close()

# Get user inputs
ip = input("Enter the IP address to scan: ")
try:
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))
    if start_port < 0 or end_port < 0 or start_port > end_port:
        raise ValueError("Invalid port range. Ensure ports are positive and the starting port is less than or equal to the ending port.")
    scan_ports(ip, start_port, end_port)
except ValueError as e:
    print(f"Error: {e}")
