"""
NetScanner - A Basic Network Scanning Tool
Author: Jonathan Perez
Date: August 27, 2024
Version: 1.0

Description:
This Python script is designed to perform basic network scanning operations, including 
identifying active IP addresses within a specified range and scanning for open ports on 
those IPs. The script uses the Scapy library to craft and send packets, then analyze 
the responses.

Usage:
- Modify the `ip_range` and `ports` variables as needed to scan different IP addresses 
  and port ranges.
- Run the script to see the results of the scan in the terminal.

Dependencies:
- Python 3.x
- Scapy (Install using: `pip install scapy`)
"""

from scapy.all import sr1, IP, TCP  # Import necessary modules from Scapy
import sys  # Import sys module for system-specific parameters and functions

def scan_ip(ip_range):
    """
    Scans a range of IP addresses to identify active hosts.
    
    Args:
    ip_range (list): List of IP addresses to scan.

    Returns:
    None
    """
    for ip in ip_range:  # Loop through each IP address in the provided range
        print(f"Scanning IP: {ip}")  # Print the IP address being scanned
        # Send a TCP SYN packet to port 80 of the target IP and wait for a response
        response = sr1(IP(dst=ip)/TCP(dport=80, flags="S"), timeout=1, verbose=0)
        if response:  # If a response is received, the IP is active
            print(f"{ip} is up and responding")

def scan_ports(ip, ports):
    """
    Scans specific ports on a given IP address to identify open ports.
    
    Args:
    ip (str): The IP address to scan.
    ports (list): List of ports to scan on the target IP.

    Returns:
    None
    """
    for port in ports:  # Loop through each port in the provided list
        # Send a TCP SYN packet to the target IP and port, and wait for a response
        response = sr1(IP(dst=ip)/TCP(dport=port, flags="S"), timeout=1, verbose=0)
        if response:  # If a response is received, the port is open
            print(f"Port {port} on {ip} is open")

if __name__ == "__main__":
    # List of IP addresses to scan (replace with the actual IP range you're interested in)
    ip_range = ["192.168.1.1", "192.168.1.2"]  
    scan_ip(ip_range)  # Call the scan_ip function to identify active hosts

    # List of ports to scan on a specific IP (replace with the actual IP and ports)
    scan_ports("192.168.1.1", [22, 80, 443])  # Call the scan_ports function to check for open ports
