terraform {
  required_providers {
    proxmox = {
      source  = "bpg/proxmox"
      version = ">= 0.40.0" # Minimum required version
    }
  }
}
provider "proxmox" {
  endpoint = "https://IP:8006/"
  insecure = true  # For Testing Only! In production, use a valid certificate!  
  api_token = "terraform@pam!terraform-token=fc8...507" # the API token must be in the format 'USER@REALM!TOKENID=UUID'
}
resource "proxmox_virtual_environment_vm" "vm-instance" {
  name      = "vm-terraform-instance" # VM name in Proxmox
  node_name = "proxmox" # Proxmox node name
  vm_id     = 500 # Unique VM ID
  clone {
    vm_id = 900 # Source template
    full  = true # Mode = Full Clone
  }
  cpu {
    cores = 2
    type = "x86-64-v2-AES" # CPU type (must be identical to the source template's CPU type)
  }
  memory {
    dedicated = 2048
  }
  disk {
    datastore_id = "local-lvm" # Proxmox storage pool name
    interface    = "scsi0" # Disk interface type (scsi/virtio)
    size         = 100 # Disk size in GB
  }
  network_device {
    model  = "virtio"
    bridge = "vmbr0" # Proxmox network bridge (default is `vmbr0`)
  }
  bios = "seabios" # BIOS type (seabios for legacy, ovmf for UEFI)
  started = false # Auto-start VM after creation? (false = no)
}
