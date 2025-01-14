import socket

def perform_dns_lookup(domain_name):
    try:
        # Get the IP address for the domain name
        ip_address = socket.gethostbyname(domain_name)
        print(f"Domain: {domain_name} -> IP Address: {ip_address}")

        # Get the host information for the IP address
        host_info = socket.gethostbyaddr(ip_address)
        print(f"IP Address: {ip_address} -> Hostname: {host_info[0]}")
        print(f"Aliases: {host_info[1]}")
        print(f"IP Addresses: {host_info[2]}")
    except socket.gaierror as e:
        print(f"Error resolving domain {domain_name}: {e}")
    except socket.herror as e:
        print(f"Error getting host info for {domain_name}: {e}")

if __name__ == "__main__":
    # Example domain names for DNS lookup
    domains = [
        "www.google.com",
        "www.facebook.com",
        "www.horizoncampus.edu.lk"
    ]

    for domain in domains:
        print(f"\nPerforming DNS lookup for: {domain}")
        perform_dns_lookup(domain)
