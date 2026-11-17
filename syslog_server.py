import socket

def start_syslog_server(host="0.0.0.0", port=514):
    print(f"[*] NOC Syslog Daemon listening on UDP {host}:{port}...")
    print("[*] Ready to ingest Cisco & Palo Alto syslog streams.")

if __name__ == "__main__":
    start_syslog_server()
