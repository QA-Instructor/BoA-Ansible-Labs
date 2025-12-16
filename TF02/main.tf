terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "7.13.0"
    }
  }
}

variable "gcp_project" {}

provider "google" {
  # Configuration options
    project = var.gcp_project
    region = "us-east1"
}

module "network" {
  source = "./network"
  network_name = "lab2-vpc"
  region = "us-east1"
  allowed_ports = ["22", "80", "8080", "8081"]
  ip_cidr_range = "10.0.1.0/24"
}

module "server" {
  source = "./instance"
  region = "us-east1"
  subnet_name = module.network.subnet_name
  machine_type = "e2-medium"
  instance_name = "app-server"
  script_path = "${path.root}/deploy.sh"
}

module "proxy" {
  source = "./instance"
  region = "us-east1"
  subnet_name = module.network.subnet_name
  machine_type = "e2-medium"
  instance_name = "proxy-server"
  script_path = "${path.root}/proxy.sh"
}