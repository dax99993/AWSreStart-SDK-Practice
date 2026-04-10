import boto3
import json
from datetime import datetime

region_name = 'us-west-2'
inventory = {
    "metadata": {
        "scan_time": datetime.now(),
        "provider": "AWS"
    },
    "ec2_instances": [],
    "s3_buckets": [],
    "lambda_functions": []
}


class DateTimeEncoder(json.JSONEncoder):
    """Custom encoder to handle AWS datetime objects in JSON."""
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super(DateTimeEncoder, self).default(obj)

def fetch_inventory():

    # Initialize Boto3 Clients
    ec2_client = boto3.client('ec2')
    s3_client = boto3.client('s3')
    lambda_client = boto3.client('lambda')

    print("Starting AWS Resource Scan...")

    # 1. Scan EC2 Instances
    try:
        instances = ec2_client.describe_instances()
        for reservation in instances.get('Reservations', []):
            for inst in reservation.get('Instances', []):
                inventory["ec2_instances"].append({
                    "id": inst['InstanceId'],
                    "type": inst['InstanceType'],
                    "state": inst['State']['Name'],
                    "launch_time": inst['LaunchTime']
                })
        print(f"Found {len(inventory['ec2_instances'])} EC2 instances.")
    except Exception as e:
        print(f"Error scanning EC2: {e}")

    # 2. Scan S3 Buckets
    try:
        buckets = s3_client.list_buckets()
        for bucket in buckets.get('Buckets', []):
            inventory["s3_buckets"].append({
                "name": bucket['Name'],
                "creation_date": bucket['CreationDate']
            })
        print(f"✔ Found {len(inventory['s3_buckets'])} S3 buckets.")
    except Exception as e:
        print(f"✘ Error scanning S3: {e}")

    # 3. Scan Lambda Functions
    try:
        functions = lambda_client.list_functions()
        for func in functions.get('Functions', []):
            inventory["lambda_functions"].append({
                "name": func['FunctionName'],
                "runtime": func['Runtime'],
                "memory": func['MemorySize'],
                "last_modified": func['LastModified']
            })
        print(f"Found {len(inventory['lambda_functions'])} Lambda functions.")
    except Exception as e:
        print(f"Error scanning Lambda: {e}")

    return inventory

def save_inventory(data, filename="aws_inventory.json"):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4, cls=DateTimeEncoder)
    print(f"\nSUCCESS: Inventory saved to {filename}")

if __name__ == "__main__":
    resource_data = fetch_inventory()
    save_inventory(resource_data)