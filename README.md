## ⌨ Provisioning a VM on Proxmox with Terraform (Linux Setup) 

![obraz](https://github.com/user-attachments/assets/b186557d-0d42-4806-84d3-5382c87f143e)

## 🧰 Prerequisites

- A Linux-based system with internet access  
- A Proxmox VE server with:
  - A pre-created VM template on Proxmox to be cloned

## 💿 Installation Terraform on LINUX
To run the Python script, install pip and the requests library using your distribution's package manager. These are needed to handle HTTP requests in the script.

🛈 **Rocky Linux / RHEL / CentOS:**
```bash
dnf install python3-pip -y && pip3 install requests
```
🛈 **Ubuntu / Debian:**
```bash
apt update && apt install -y python3-pip python3-requests
```
🏎️💨 **Install Terraform Automatically**

This repository includes a Python script that installs the latest available version of Terraform from the official HashiCorp releases.

1️⃣ Make the script executable:
```bash
chmod +x install_terraform.py
```
2️⃣ Run it as root:
```bash
./install_terraform.py
```

☝️ Note: You must run this script as root, because it installs the Terraform binary into /usr/local/bin
