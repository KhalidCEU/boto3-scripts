import boto3

ec2 = boto3.client('ec2')

subnets = ec2.describe_subnets()

print("ALL SUBNETS\n")
for subnet in subnets.get('Subnets'):
    print(f"Subnet Id: {subnet.get('SubnetId')}")
    print(f"VPC Id: {subnet.get('VpcId')}")
    print(f"CIDR Block: {subnet.get('CidrBlock')}")

    autoPublicIp = 'yes' if subnet.get('MapPublicIpOnLaunch') else 'no'
    print(f"Public IP on launch: {autoPublicIp}")

    print()