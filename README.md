# 🚨 NOC Syslog Collector & Incident Parser

A UDP Syslog listener (Port 514) that ingests, parses, and formats incoming event logs from Cisco IOS and Palo Alto PAN-OS appliances.

## 📌 Syslog Severity Classification
- Level 0: Emergency (System unusable)
- Level 1: Alert (Immediate action required)
- Level 2: Critical
- Level 3: Error
- Level 4: Warning (Interface link flaps, high memory)
- Level 5: Notification (Config changes, OSPF neighbor adjacency change)
- Level 6: Informational
