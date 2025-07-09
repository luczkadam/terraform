#!/usr/bin/env python3

import os			#used for: checking the user ID
import sys			#used for: exiting the program with sys.exit()
import shutil		#used for: copying/moving files and checking executable locations
import subprocess	#used for: installing missing packages
import requests		#used for: send an HTTP GET request to download the Terraform ZIP file
import time			#used for: adding delays
import zipfile		#used for: extracting .zip files

def check_root():
    if os.geteuid() != 0:
        print("⛔ This script must be run as root.")
        sys.exit(1)

def ensure_tools_installed():
    tools = ["wget", "nano", "unzip"]
    if shutil.which("dnf"):
        installer = ["dnf", "install", "-y"]
    elif shutil.which("yum"):
        installer = ["yum", "install", "-y"]
    elif shutil.which("apt"):
        installer = ["apt", "install", "-y"]
    else:
        print("⛔ No supported package manager found (dnf/yum/apt).")
        sys.exit(1)

    for tool in tools:
        if shutil.which(tool) is None:
            print(f"🔨 Installing missing tool: {tool}")
            subprocess.run(installer + [tool], check=True)
        else:
            print(f"👍 {tool} is installed.")
    time.sleep(2)

def fetch_latest_version():
    print("🌍 Checking for the latest Terraform version...")
    url = "https://checkpoint-api.hashicorp.com/v1/check/terraform"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        latest = response.json()["current_version"]
        print(f"👍 Latest version: {latest}")
        time.sleep(2)
        return latest
    except requests.exceptions.RequestException as e:
        print(f"⛔ Error fetching the latest version: {e}")
        sys.exit(1)

def download_terraform(version):
    filename = f"terraform_{version}_linux_amd64.zip"
    url = f"https://releases.hashicorp.com/terraform/{version}/{filename}"
    print(f"📥 Downloading Terraform {version} from {url}")
    try:
        response = requests.get(url, timeout=60)
        response.raise_for_status()
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"💾 Saved as {filename}")
        time.sleep(2)
        return filename
    except requests.exceptions.RequestException as e:
        print(f"⛔ Error downloading the Terraform file: {e}")
        sys.exit(1)

def unzip_file(zip_name):
    print("✄┈┈┈┈ Unzipping Terraform binary...")
    target_dir = "TERRAFORM"
    os.makedirs(target_dir, exist_ok=True)
    with zipfile.ZipFile(zip_name, 'r') as zip_ref:
        zip_ref.extractall(target_dir)
    print(f"👍 Unzipped to ./{target_dir}/ directory")
    time.sleep(2)
    return os.path.join(target_dir, "terraform")

def set_owner(path):
    print(f"🔑 Setting owner to root:root for {path}")
    try:
        subprocess.run(["chown", "root:root", path], check=True)
        time.sleep(2)
    except subprocess.CalledProcessError as e:
        print(f"⛔ Failed to set owner for {path}: {e}")
        sys.exit(1)

def copy_binary(source, target="/usr/local/bin/terraform"):
    print(f"✈️ Copying binary to {target}")
    try:
        shutil.copy(source, target)
        subprocess.run(["chmod", "+x", target], check=True)
        time.sleep(2)
    except (shutil.Error, subprocess.CalledProcessError) as e:
        print(f"⛔ Error while copying the binary: {e}")
        sys.exit(1)

def verify_installation():
    print("👀 Verifying installation...")
    result = subprocess.run("command -v terraform", shell=True, capture_output=True, text=True)
    path = result.stdout.strip()
    if path == "/usr/local/bin/terraform":
        print(f"👍 Terraform successfully installed at {path}")
        version_result = subprocess.run(["terraform", "--version"], capture_output=True, text=True)
        print(f"🛈 Version: {version_result.stdout.strip().splitlines()[0]}")
    else:
        print("⛔ Terraform not found in /usr/local/bin/")
        sys.exit(1)
    time.sleep(2)

def archive_zip_file(zip_filename, target_dir="TERRAFORM"):
    try:
        destination = os.path.join(target_dir, zip_filename)
        shutil.move(zip_filename, destination)
        print(f"👍 ZIP file moved to {destination}")
    except shutil.Error as e:
        print(f"⛔ Could not move the ZIP file (it might already be there): {e}")

if __name__ == "__main__":
    check_root()
    ensure_tools_installed()
    version = fetch_latest_version()
    time.sleep(1)
    zip_file = download_terraform(version)
    time.sleep(1)
    binary_path = unzip_file(zip_file)
    set_owner(binary_path)
    copy_binary(binary_path)
    verify_installation()
    archive_zip_file(zip_file) 
    print("\n😁👍🆗 All done!")