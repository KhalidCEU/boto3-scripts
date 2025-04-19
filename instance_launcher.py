import sys
import boto3

def main (image_id, instance_type, subnet_id, has_public_ip,
    security_group_name, key_name) :

    ec2_res = boto3.resource('ec2')
    ec2_client = boto3.client('ec2')

    # Get security group ID by its name
    sg_response = ec2_client.describe_security_groups(
        Filters=[{'Name': 'group-name', 'Values': [security_group_name]}]
    )

    if not sg_response['SecurityGroups']:
        raise Exception(f"Security group not found: {security_group_name}")

    sg_id = sg_response['SecurityGroups'][0]['GroupId']

    # Network configuration
    network_interfaces = [{
        'SubnetId': subnet_id,
        'DeviceIndex': 0,
        'AssociatePublicIpAddress': True if has_public_ip.lower() == 'yes' else False,
        'Groups': [sg_id]
    }]

    # Create instance
    instances = ec2_res.create_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        KeyName=key_name,
        MinCount=1,
        MaxCount=1,
        NetworkInterfaces=network_interfaces
    )

    instance = instances[0]
    instance.wait_until_running()  # Wait for the instance to have 'running' state
    instance.reload()

    print(f"New instance ID: {instance.id}")
    print(f"State: {instance.state['Name']}")


    return 0


def usage(exitstatus):
    print(
        "Usage: python3 instance_launcher.py"
        "<image_id> <instance_type> <subnet_id> <has_public_ip> <security_group_name> <key_name>"
    )
    sys.exit(exitstatus)

if __name__ == "__main__":
    if sys.argv[1] == "-h":
        usage(0)
    if len(sys.argv) != 7 :
        usage(1)
    main(*sys.argv[1:])
