variable "docker_image" {
  description = "Docker image name"
  type        = string
  default     = "supernutman/note-api:latest"
}

variable "container_name" {
  description = "Container name"
  type        = string
  default     = "note-api-terraform"
}

variable "external_port" {
  description = "External port"
  type        = number
  default     = 5001
}