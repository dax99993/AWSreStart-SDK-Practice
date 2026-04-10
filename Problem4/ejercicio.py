import boto3
from datetime import datetime, timezone, timedelta

# SETUP
BUCKET_NAME = 'my-bucket-dbt99'
MAX_DAYS = 30

def clean_s3_bucket():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(BUCKET_NAME)
    now = datetime.now(timezone.utc)
    limit = now - timedelta(days=MAX_DAYS)

    print(f"Search for objects modified before: {limit}")

    # List objects
    for my_object in bucket.objects.all():
        if my_object.last_modified < limit:
            print(f"Deleting: {my_object.key} (Modified: {my_object.last_modified})")
            # uncomment to actually delete file
            # my_object.delete()

if __name__ == "__main__":
    clean_s3_bucket()