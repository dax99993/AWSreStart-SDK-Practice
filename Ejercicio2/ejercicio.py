import boto3
import time
import os

bucket_name = 'my-bucket-dbt99'
base_path = "/workspaces/mex30-sdk/Ejercicio2/"
folder_name = 'folder_to_backup'

def main():
    # Crear un cliente de S3
    s3 = boto3.client('s3')

    try:
        s3.head_bucket(Bucket=bucket_name)
        # print(f"Bucket '{bucket_name}' already exists.")
    except s3.exceptions.ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            print(f"Creating bucket '{bucket_name}'...")
            s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': s3.meta.region_name})
            print(f"Bucket '{bucket_name}' created successfully.")
        else:
            print(f"Error verifying the bucket: {e}")

    # Verify folder existence
    folder_path = os.path.join(base_path, folder_name)
    if os.path.exists(folder_path):
        print(f"Folder '{folder_name}' exists.")
    else:
        print(f"Folder '{folder_name}' does not exist.")
        exit(1)

    # Upload files to S3
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            s3_key = os.path.relpath(file_path, base_path)
            print(f"Uploading '{file_path}' to S3 bucket '{bucket_name}' with key '{s3_key}'...")
            s3.upload_file(file_path, bucket_name, s3_key)
            print(f"File '{file_path}' uploaded successfully.")


if __name__ == "__main__":
    main()