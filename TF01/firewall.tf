resource "google_compute_firewall" "lab-firewall" {
  name    = "custom-firewall"
  network = google_compute_network.lab-vpc.name

  allow {
    protocol = "tcp"
    ports    = ["8080", "8081"]
  }

  source_ranges = ["0.0.0.0/0"]
}
