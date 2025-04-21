import sys
import boto3

def main (instance_ids) :
    print("INSTANCE KILLER\n")

    ec2_res = boto3.resource('ec2')

    for instance_id in instance_ids:
        instance = ec2_res.Instance(instance_id)
        print(f"Terminating instance {instance_id} ...")
        instance.terminate()                # Terminate the instance
        instance.wait_until_terminated()
        instance.reload()                   # Update instance data
        print(f"Instance {instance.id} succesfully terminated !")
        print(f"State: {instance.state['Name']}")
        print()

    return 0


def usage(exitstatus):
    print(
        "Usage: python3 instance_killer.py <instance1_id> <instance2_id> <instance3_id>..."
    )
    sys.exit(exitstatus)

if __name__ == "__main__":
    if sys.argv[1] == "-h":
        usage(0)
    if len(sys.argv) <= 1 :
        usage(1)
    main(sys.argv[1:])
