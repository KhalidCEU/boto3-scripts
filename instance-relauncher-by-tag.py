import sys
import boto3

def main (tag_key) :
    print("INSTANCE RELAUNCHER (by tag)")

    ec2_res = boto3.resource('ec2')
    ec2 = boto3.client('ec2')

    # Gets Reservations containing instances with 'stopped' state name
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': [ 'stopped']
            }
        ]
    )

    # Get the list of instances form the Reservations
    instances = [
        inst
        for reservation in response['Reservations']
        for inst in reservation['Instances']
    ]

    found_tag = False

    print(f'Checking instances...')

    for instance in instances:
        instance_id = instance.get('InstanceId')
        instance = ec2_res.Instance(instance_id)

        # Check if the instance has any tag with the specified Tag Key
        for tag in instance.tags or []:
            if tag['Key'] == tag_key:
                found_tag = True
                break

        if found_tag:
            print(f'Found instance {instance.id} with this Tag Key!')
            print(f'Launching instance ...')
            instance.start()
            instance.wait_until_running()
            print(f'Instance launched !')
            print(f"State: {instance.state['Name']}")
            print()
            found_tag = False

    print("All stopped instances have been checked !")
    return 0


def usage(exitstatus):
    print(
        "Usage: python3 instance-relauncher-by-tag.py <tag_key>"
    )
    sys.exit(exitstatus)

if __name__ == "__main__":
    if "-h" in sys.argv:
        usage(0)
    if len(sys.argv) != 2:
        usage(1)
    main(*sys.argv[1:])


