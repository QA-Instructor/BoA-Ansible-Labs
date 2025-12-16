
resource "google_compute_instance" "vm1" {
  name         = "demo-instance-1"
  machine_type = "e2-medium"
  zone         = "us-east1-b"

  allow_stopping_for_update = true

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-12"
    }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.lab-subnet.name


    access_config {
      // Ephemeral public IP
      network_tier = "STANDARD"
    }
  }
  
  metadata_startup_script = file("deploy.sh")

}
