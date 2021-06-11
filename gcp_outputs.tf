/*
 * Terraform output variables for GCP.
 */

output "cloud_run_service_name" {
  value = google_cloud_run_service.getToken.name
}




