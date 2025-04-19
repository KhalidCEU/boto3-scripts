import boto3

ec2 = boto3.client('ec2')
elb = boto3.client('elb')
elbv2 = boto3.client('elbv2')

# Balanceadores
lbs_v1 = elb.describe_load_balancers()
lbs_v2 = elb.describe_load_balancers()
nb_classic_lbs = len(lbs_v1.get('LoadBalancerDescriptions', []))
nb_other_lbs = len(lbs_v2.get('LoadBalancers', []))

nb_total_lbs = nb_classic_lbs + nb_other_lbs

# Instantaneas
snapshots = ec2.describe_snapshots(OwnerIds=['self'])
nb_snapshots = len(snapshots.get('Snapshots', []))

# Grupos de seguridad
security_groups = ec2.describe_security_groups()
nb_security_groups = len(security_groups.get('SecurityGroups', []))

# Volumenes
volumes = ec2.describe_volumes()
nb_volumes = len(volumes.get('Volumes', []))

# Claves
key_pairs = ec2.describe_key_pairs()
nb_key_pairs = len(key_pairs.get('KeyPairs', []))

print("SUMMARY - Ressource Count\n")

print(f"Volumes:\t\t", nb_volumes)
print(f"Snapshots:\t\t", nb_snapshots)
print(f"Security Groups:\t", nb_security_groups)
print(f"Load balancers:\t\t", nb_total_lbs)
print(f"Key Pairs:\t\t", nb_key_pairs)
