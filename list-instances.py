import boto3

ec2 = boto3.client('ec2')

non_terminated_instances = ec2.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [ 'pending', 'running', 'shutting-down',
                    'stopping', 'stopped'
            ]
        }
    ]
)

print("NON-TERMINATED INSTANCES\n")
for reservations in non_terminated_instances.get('Reservations', []):
    for instance in reservations.get('Instances', []):
        print(f"Instance ID: {instance.get('InstanceId')}")
        print(f"State: {instance.get('State').get('Name')}")
        print(f"Image (AMI) Id: {instance.get('ImageId')}")
        print(f"Subnet Id: {instance.get('SubnetId')}")
        print(f"Key Name: {instance.get('KeyName')}")

        sg_names = [sg['GroupName'] for sg in instance.get('SecurityGroups', [])]
        print(f"Security groups: {', '.join(sg_names)}")

        print(f"Private IP address: {instance.get('PrivateIpAddress')}")

        public_ip = instance.get('PublicIpAddress')
        if public_ip:
            print(f"Public IP address: {public_ip}")

        print()
