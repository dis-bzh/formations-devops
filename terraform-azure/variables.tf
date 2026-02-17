variable "prefix" {
  description = "Prefix for all resource names"
  type        = string
  default     = "vde"
}

variable "location" {
  description = "Azure Region"
  type        = string
  default     = "West Europe"
}

variable "admin_username" {
  description = "Admin username for the VMs"
  type        = string
  default     = "devops"
}

variable "ssh_public_key_path" {
  description = "Path to the SSH public key file"
  type        = string
  default     = "/home/vde/.ssh/id_ed2551_azure_cesi_vde.pub"
}

variable "vm_size" {
  description = "Size of the VMs"
  type        = string
  default     = "Standard_B2ts_v2"
}

variable "allowed_ssh_cidr" {
  description = "CIDR block allowed to SSH into the bastion (e.g. your public IP as x.x.x.x/32)"
  type        = string
  default     = "*" # ⚠️ Restrict this in production!
}

variable "tags" {
  description = "Tags to apply to all resources"
  type        = map(string)
  default = {
    environment = "training"
    project     = "formations-devops"
    managed_by  = "terraform"
  }
}
