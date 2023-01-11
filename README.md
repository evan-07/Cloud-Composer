# Cloud-Composer
This is a repository for practicing using Google Cloud Composer (Airflow)

Buckets Created:
cc_ivan_us
cc_ivan_eu




DAGS_COPY_CSV=dags_bq_copy_eu_to_us_sample.csv

DAGS_BUCKET=$(gsutil ls -l | grep composer)
gsutil cp -r gs://spls/gsp283/python-docs-samples/third_party/apache-airflow/plugins/* gs://$DAGS_BUCKET/plugins

GCS_SOURCE_BUCKET=cc_ivan_us
GCS_DEST_BUCKET=-cc_ivan_eu

