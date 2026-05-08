terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "note_api" {
  name         = "supernutman/note-api:latest"
  keep_locally = true
}

resource "docker_container" "note_api" {
  name  = "note-api-terraform"
  image = docker_image.note_api.image_id

  ports {
    internal = 5000
    external = 5001
  }

  networks_advanced {
    name = "note-api_devops-net"
  }
}