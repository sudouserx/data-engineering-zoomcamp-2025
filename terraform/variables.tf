variable "credentials" {
  description = "Project Credentials"
  default     = "./keys/cred.json"
}

variable "project" {
  description = "Project Name"
  default     = "lithe-record-447616-m6"
}

variable "region" {
  description = "Project Deployment Region"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "Bigquery dataset name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "Storage Bucket Name"
  default     = "lithe-record-447616-m6-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}