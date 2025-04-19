import sys
import boto3

def main (instance_id, tag_key, tag_value) :
    ec2_res = boto3.resource('ec2')

    instance = ec2_res.Instance(instance_id)

    # Añadir / actualizar la etiqueta
    instance.create_tags(Tags=[{'Key': tag_key, 'Value': tag_value}])

    # Obtener ID de la imagen (AMI)
    image_id = instance.image_id

    # Obtenemos todas las etiquetas de la instancia
    instance.load()  # Actualizamos los datos (para obtener la nueva etiqueta tambien)
    tags = instance.tags or []

    print(f"Image (AMI) Id: {image_id}")
    print("Associated tags:")
    for tag in tags:
        print(f"  {tag['Key']}: {tag['Value']}")

    return 0

def usage(exitstatus):
    print(
        "Usage: python3 instance_tagger.py <instance_id> <tag_key> <tag_value>"
    )
    sys.exit(exitstatus)

if __name__ == "__main__":
    if "-h" in sys.argv:
        usage(0)
    if len(sys.argv) != 4 :
        usage(1)
    main(*sys.argv[1:])

