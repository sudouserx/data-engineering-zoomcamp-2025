terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.19.0"
    }
  }
}

provider "google" {
  credentials = "./keys/cred.json"
  project     = "lithe-record-447616-m6"
  region      = "asia-south1"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "lithe-record-447616-m6-terra-bucket"
  location      = "ASIA"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 3   # 3 days 
    }
    action {
      type = "Delete"
    } 
  }
}

