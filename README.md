# 🚨 AI-SOC & SIEM Threat Detection & Incident Response Lab

A security operations center (SOC) toolkit featuring custom **Wazuh SIEM detection rules**, real-time Syslog ingestion, and production **Incident Response Playbooks** mapped to the MITRE ATT&CK framework.

## 📌 Roadmap Alignment: Networkers Home Cyber & Cloud Security
- **Domain:** AI-SOC (Security Operations Center) & SIEM (Splunk / Wazuh)
- **Incident Response Playbooks:** Step-by-step triage for Brute-Force and C2 malware beaconing
- **SIEM Rules:** Custom XML detection rules for MITRE ATT&CK techniques (T1110, T1548, T1071)
- **Centralized Ingestion:** UDP Syslog daemon capturing events from Linux endpoints, Cisco routers, and Palo Alto firewalls

## 📁 Repository Contents
- `wazuh_detection_rules.xml`: Custom SIEM correlation rules for threat identification.
- `soc_incident_response_playbook.md`: Standard Operating Procedures (SOP) for SOC L1/L2 analysts.
- `syslog_server.py`: Python syslog listener for multi-vendor network event ingestion.

---
*Created by Manoj M | Network & Cyber Security Engineer*
