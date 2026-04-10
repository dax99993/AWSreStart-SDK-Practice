import boto3
import random
import time

namespace = 'Alerts/',


def upload_custom_metric(metric_value, metric_name='ProcessedFiles'):
    # Create CloudWatch client
    cloudwatch = boto3.client('cloudwatch', region_name='us-west-2')

    try:
        response = cloudwatch.put_metric_data(
            Namespace=namespace,
            MetricData=[
                {
                    'MetricName': metric_name,
                    'Dimensions': [
                        {'Name': 'Environment', 'Value': 'Production'},
                        {'Name': 'Service', 'Value': 'ProcessedFiles'}
                    ],
                    'Value': metric_value,
                    'Unit': 'Count'
                },
            ]
        )
        #print(response)
        print(f"Metric '{metric_name}' upload value: {metric_value}")
    except Exception as e:
        print(f"Error while uploading metric: {e}")


if __name__ == "__main__":
    while True:
        # Generate a random value (simulation)
        value= random.randint(1, 100)
        upload_custom_metric(value)

        print("Wait 1 minute for next value...")
        time.sleep(60)
