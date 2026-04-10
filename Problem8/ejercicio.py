import boto3
import json
import os

# Initialize S3 client
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # 1. Capture the source bucket and file name from the event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']

    # Define the destination bucket (stored in an Environment Variable)
    destination_bucket = os.environ.get('DEST_BUCKET', 'my-processed-results-bucket')

    try:
        print(f"Processing file: {file_key} from bucket: {source_bucket}")

        # 2. Read the content of the file
        response = s3_client.get_object(Bucket=source_bucket, Key=file_key)
        content = response['Body'].read().decode('utf-8')

        # 3. Process the content (Example: Count lines)
        line_count = len(content.splitlines())
        result_text = f"The file '{file_key}' has {line_count} lines."

        # 4. Save the result to the destination bucket
        result_key = f"results/processed_{file_key}.txt"
        s3_client.put_object(
            Bucket=destination_bucket,
            Key=result_key,
            Body=result_text
        )

        print(f"Successfully processed and saved to: {result_key}")

        return {
            'statusCode': 200,
            'body': json.dumps('File processed successfully!')
        }

    except Exception as e:
        print(f"Error: {e}")
        raise e

if __name__ == '__main__':
    print("Lambda ")
    # lambda_handler(None, None)