output "container_name" {
  value = docker_container.note_api.name
}

output "container_port" {
  value = var.external_port
}