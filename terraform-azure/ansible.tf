resource "local_file" "ansible_inventory" {
  content = templatefile("${path.module}/inventory.tmpl", {
    bastion_ip = azurerm_public_ip.bastion_pip.ip_address,
    app_ip     = azurerm_network_interface.app_nic.private_ip_address,
    username   = var.admin_username
  })
  filename = "${path.module}/inventory"
}
