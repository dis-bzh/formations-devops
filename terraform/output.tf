output "vms" {
  value     = resource.warren_virtual_machine.denvr_vms
  sensitive = true
}

output "public_ips" {
  value = resource.warren_floating_ip.denvr_ip
}

resource "local_file" "ansible_inventory" {
  content = templatefile("${path.module}/inventory.tmpl", {
    vms = resource.warren_virtual_machine.denvr_vms
    public_ips = resource.warren_floating_ip.denvr_ip
  })
  filename = "${path.module}/inventory"
}
