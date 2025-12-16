
resource "google_compute_instance" "vm" {
  name         = var.instance_name
  machine_type = var.machine_type
  zone         = "${var.region}-b"

  allow_stopping_for_update = true

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-12"
    }
  }

  network_interface {
    subnetwork = var.subnet_name


    access_config {
      // Ephemeral public IP
      network_tier = "STANDARD"
    }
  }
  
  metadata_startup_script = file(var.script_path)

}
