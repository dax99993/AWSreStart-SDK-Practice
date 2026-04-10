import boto3
from datetime import datetime

def create_ebs_snapshots():
    # Initialize the EC2 client
    ec2 = boto3.client('ec2', region_name='us-west-2')

    print(f"--- Starting Snapshot Process: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")

    try:
        # 1. List all EBS volumes in the region
        volumes = ec2.describe_volumes()

        for volume in volumes['Volumes']:
            vol_id = volume['VolumeId']
            state = volume['State']

            print(f"Found Volume: {vol_id} (State: {state})")

            # 2. Create Snapshot
            description = f"Automated snapshot of {vol_id} created on {datetime.now().isoformat()}"

            snapshot = ec2.create_snapshot(
                VolumeId=vol_id,
                Description=description,
                TagSpecifications=[
                    {
                        'ResourceType': 'snapshot',
                        'Tags': [
                            {'Key': 'Name', 'Value': f"Backup-{vol_id}"},
                            {'Key': 'CreatedBy', 'Value': 'AutomationScript'}
                        ]
                    }
                ]
            )

            print(f"Successfully triggered snapshot: {snapshot['SnapshotId']}")

    except Exception as e:
        print(f"Error encountered: {e}")

if __name__ == "__main__":
    create_ebs_snapshots()