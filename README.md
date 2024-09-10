# Site test project
## A small Django project
Website made entirely using Django backend and frontend (HTML and CSS)

### Dependencies
Refer to the requirements.txt located in the top-level fodler of the project.

### Running the project
In debug mode, you can simply run with this command and folowe the given URL:
```
python manage.py runserver
```

For production, please follow the instruction to your specific hosting platform to prepare all the variables and configurations.

### Google Cloud Run
This project was adapted to GCR based on [this guide](https://cloud.google.com/python/django/run). The needed services are:
- Cloud Run
- Artifact Registry

For simplicity's sake, container environment variables were used instead of Secret Manager, and the sqlite3 database was kept as is instead of migrating to PostgreSQL (due to not being able to containerize or put the db file in a volume successfully). Not ideal changes, but this docker/gcr test was mostly a litmus test for the service with my current projects.

In order to host the services needed for the project, in short:
- Build the image using the `cloudmigrate.yaml` file with the `gcloud builds submit`
- Deploy the service at first, using the complete `gcloud run deploy name-of-service`
- Once you have the url, create environment variables through either the gcloud cli or the GCR console > Service > Revisions > Variables
- Update the GCR service by setting the environment variables needed, in this case `IS_DEV=False` and `APP_HOST=url-of-website.here`
    - Note that the url most not have the scheme, which mean it shouldnot have http, https or ending slash.
- To finalize the update process, just run the Cloud Build and migration script once again, and deploy the service again with the region and image.