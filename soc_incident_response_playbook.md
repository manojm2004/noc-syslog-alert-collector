# 🛡️ SOC Analyst L1/L2 Incident Response Playbook

Standard Operating Procedures (SOP) for Triaging, Investigating, and Remediating Security Incidents.

---

## 🚨 Incident 1: SSH Brute-Force Attack (MITRE ATT&CK T1110)
### Triage & Verification
1. Inspect SIEM alert details: Identify Source IP, Target Server, and Timestamp.
2. Verify log in `/var/log/auth.log` or Windows Security Event ID `4625` (Failed Logon).
3. Check if any attempt succeeded (Event ID `4624` or `Accepted password` for user).

### Containment & Eradication
- **Immediate Action:** Block Source IP on perimeter firewall (Palo Alto NGFW Security Policy or drop rule).
- **Endpoint Action:** Check if `fail2ban` banned the IP. If not, trigger temporary IPtable drop:
  ```bash
  sudo iptables -A INPUT -s <Attacker_IP> -j DROP
  ```
- **Post-Incident:** Enforce SSH Key-Only Authentication (`PasswordAuthentication no`) and change default port 22.

---

## 🚨 Incident 2: Malware / C2 Beaconing Detected by Palo Alto NGFW
### Triage & Verification
1. Query Palo Alto PAN-OS Threat Logs (`Monitor -> Logs -> Threat`).
2. Identify infected host internal IP, domain name accessed, and WildFire verdict.

### Containment & Remediation
- **Isolate Host:** Move client switchport to an isolated quarantine VLAN (VLAN 666).
- **DNS Sinkholing:** Verify PAN-OS sinkhole intercepted subsequent queries.
- **Forensic Capture:** Extract memory dump and network PCAP for hash matching on VirusTotal.
