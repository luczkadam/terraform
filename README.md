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

This repository includes a Python script that installs the latest available AMD64 version of Terraform from the official HashiCorp releases.

1️⃣ Download the script using the following command:
```bash
wget https://raw.githubusercontent.com/luczkadam/terraform/main/install_terraform.py
```
2️⃣ Make the script executable:
```bash
chmod +x install_terraform.py
```
3️⃣ Run it as root:
```bash
./install_terraform.py
```

☝️ Note: You must run this script as root, because it installs the Terraform binary into /usr/local/bin



## 👨🏻‍💻 Proxmox Terraform User Setup Script
This script automates the configuration of a Proxmox VE server for Terraform integration. It creates a dedicated user, role, and group with configured permissions, enabling secure API access for infrastructure automation.

🛈 **When executed, the script performs the following actions:**
1. Create a user named terraform
2. Create a role named terraform with necessary permissions
3. Create a group named terraform
4. Assign appropriate permissions to the terraform group
5. Add the terraform user to the terraform group
6. Generate an API token for the terraform user
   
☝️ Note: The token secret is displayed only once. Make sure to copy it and store it in a secure place, such as a password manager, as it cannot be retrieved again.

![terraform2_fc8e583f-e752-4ad1-ab22-0ca8619ee507](https://github.com/user-attachments/assets/2b6ba1a6-dcc6-42bd-ae40-3d30319b1edc)

1️⃣ Open a shell on your Proxmox server

Run these commands directly on the Proxmox node, either via SSH or the built-in web shell in the Proxmox GUI.
```bash
wget https://raw.githubusercontent.com/luczkadam/terraform/main/user_terraform.py
```
2️⃣ Make the script executable:
```bash
chmod +x user_terraform.py
```
3️⃣ Run it as root:
```bash
./user_terraform.py
```
4️⃣ Save the API token:
```
Once the script completes, it will output a newly generated API token.
☝️ Note: The token secret is displayed only once.
```
