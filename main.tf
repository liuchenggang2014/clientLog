provider "google" {
  project = var.project-name
  region  = var.region
}



#1. deploy cloud run service with noauth
# google_cloudrun_service creates a Managed Google Cloud Run Service.
resource "google_cloud_run_service" "getToken" {
  name     = "get-pubsub-token"
  location = var.region

  template {
    spec {
      containers {
        image = var.image-name
        ports {
          # name = "flask"
          # protocol = "tcp"
          container_port = 3000
        }
      }

      # add it if you need a customized service account with your cloud run, otherwise your cloud 
      # run will use default cloud run's service account
      service_account_name = var.sa-mail
    }
  }
}

#2. setup a noauth google_iam_policy 
data "google_iam_policy" "noauth" {
  binding {
    role = "roles/run.invoker"
    members = [
      "allUsers",
    ]
  }
}

#3. bind the cloud run service to noauth iam policy
# Authoritative. Sets the IAM policy for the service and replaces 
# any existing policy already attached.
resource "google_cloud_run_service_iam_policy" "noauth" {
  location    = google_cloud_run_service.getToken.location
  project     = google_cloud_run_service.getToken.project
  service     = google_cloud_run_service.getToken.name

  policy_data = data.google_iam_policy.noauth.policy_data
}