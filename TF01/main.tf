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