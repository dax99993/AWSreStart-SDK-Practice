import boto3
from datetime import datetime
import os

def main():
    # Crear un cliente de EC2
    ec2_client = boto3.client('ec2', region_name='us-west-2')
    # ec2_resource = boto3.resource('ec2')

    try:
        response = ec2_client.describe_instances()
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                print(f"ID: {instance['InstanceId']}, State: {instance['State']['Name']}")
        print(response)
    except ec2_client.exceptions.ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            print(f"Not found")
        else:
            print(f"Error verifying operation: {e}")

if __name__ == "__main__":
    main()