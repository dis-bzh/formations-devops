output "resource_group_name" {
  description = "Name of the Azure Resource Group"
  value       = azurerm_resource_group.rg.name
}

output "bastion_public_ip" {
  description = "Public IP address of the bastion host"
  value       = azurerm_public_ip.bastion_pip.ip_address
}

output "app_private_ip" {
  description = "Private IP address of the application VM"
  value       = azurerm_network_interface.app_nic.private_ip_address
}

output "nat_gateway_ip" {
  description = "Public IP used by the NAT Gateway for outbound traffic"
  value       = azurerm_public_ip.nat_pip.ip_address
}
