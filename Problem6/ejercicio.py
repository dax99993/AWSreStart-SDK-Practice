import boto3
# import json

# Configuration
USER_LIST = ["dev_user_01", "dev_user_02", ]
POLICY_ARN = "arn:aws:iam::aws:policy/ReadOnlyAccess"

def create_iam_users():
    # Initialize IAM client
    iam = boto3.client('iam')

    for user_name in USER_LIST:
        print(f"--- Processing User: {user_name} ---")

        try:
            # 1. Create the User
            iam.create_user(UserName=user_name)
            print(f"Successfully created user: {user_name}")

            # 2. Attach Managed Policy
            iam.attach_user_policy(
                UserName=user_name,
                PolicyArn=POLICY_ARN
            )
            print(f"Attached policy: {POLICY_ARN}")

            # 3. Create Access Keys
            response = iam.create_access_key(UserName=user_name)
            access_key = response['AccessKey']

            # Output the credentials
            # TODO: In production, save these securely (e.g., AWS Secrets Manager)
            print(f"Access Key ID: {access_key['AccessKeyId']}")
            print(f"Secret Access Key: {access_key['SecretAccessKey']}")
            print(f"Status: {access_key['Status']}")

        except iam.exceptions.EntityAlreadyExistsException:
            print(f"Skipping: User {user_name} already exists.")
        except Exception as e:
            print(f"Error creating {user_name}: {e}")

        print("\n")


if __name__ == "__main__":
    create_iam_users()