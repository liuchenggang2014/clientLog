# clientLog


## steps

1. create the terraform gcloud build image
2. change the substitution in cloudbuild.yaml
    - _BUCKET: specifiy the terraform's state file in gcs
    - _REGION: cloud run's deployment region, default is us-central1
    - _IMAGE_NAME: image name in your project
3. create a service account and download your key into ./app directory
4. create a table for pub/sub into bq
```
bq mk \
--table \
cliu201:ds201.mobilelog2 \
id:string,price:string,product:string
```
5. create the pubsub topic into bigquery dataflow template
- source: pubsub topic
- destination: bq tale in step4
- temp gcs location for temp file for dataflow
