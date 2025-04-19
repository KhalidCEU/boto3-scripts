import sys
import boto3

def main (tag_key) :
    print("INSTANCE RELAUNCHER (by tag)")

    ec2_res = boto3.resource('ec2')
    ec2 = boto3.client('ec2')

    # Obtenemos reservaciones que tienen instancias con estado 'stopped'
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': [ 'stopped']
            }
        ]
    )

    # Obtenemos lista de instancias
    instances = [
        inst
        for reservation in response['Reservations']
        for inst in reservation['Instances']
    ]

    # Creamos un boolean para saber si lanzar o no
    found_tag = False

    print(f'Analizando instancias...')

    for instance in instances:
        instance_id = instance.get('InstanceId')
        instance = ec2_res.Instance(instance_id)

        # Vemos si alguno de los tags contiene esa clave (tag_KEY)
        for tag in instance.tags or []:
            if tag['Key'] == tag_key:
                found_tag = True
                break

        if found_tag:
            print(f'La instancia {instance.id} tiene esta etiqueta!')
            print(f'Lanzando instancia ...')
            instance.start()
            instance.wait_until_running()  # Esperamos a que la instancia tenga estado 'running'
            print(f'Instancia lanzada !')
            print(f"State: {instance.state['Name']}")
            print()
            found_tag = False # Restablecemos a false para la proxima iteracion

    print("Todas las instancias con estado 'stopped' han sido analizadas !")
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


