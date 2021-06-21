# clientLog


## steps

1. create the terraform gcloud build image in your own project
```
cd terraform
gcloud builds submit
```
2. create a service account and give it the pub/sub permission
3. give the cloud build default service account(project-number@cloudbuild.gserviceaccount.com) the cloud run admin and service account user permission at least
4. change the substitution in cloudbuild.yaml
    - _BUCKET: specifiy the terraform's state file in gcs
    - _REGION: cloud run's deployment region, default is us-central1
    - _IMAGE_NAME: image name in your project
    - _SA_MAIL: Service account email bind to the cloud run services
```
cd getToken
gcloud builds submit
```
5. create a table for pub/sub into bq, which have the same schema with the log
```
bq mk \
--table \
cliu201:ds201.mobilelog2 \
id:string,price:string,product:string
```
6. create the pubsub topic into bigquery dataflow template
- source: pubsub topic
- destination: bq tale in step4
- temp gcs location for temp file for dataflow
