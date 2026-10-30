server_ip = ("192", "168", "1", "10")
allowed_ips = ["192.168.1.2", "192.168.1.3"]

def update_allowed_ips(ip):
    allowed_ips.append(ip)
    print("IP added successfully")

def display_configuration():
    print("Server IP:", ".".join(server_ip))
    print("Allowed IPs:", allowed_ips)


update_allowed_ips("192.168.1.4")

display_configuration()

# server_ip cannot be directly changed because it is a tuple
