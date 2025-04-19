# AWS Boto3 Scripts

## Setup
First **install dependencies** with:
```
pip install -r requirements.txt
```

## Usage

You can then use the scripts like this :

### Instance Launcher

**Launches** an instance by providing:
- **AMI** ID
- Instance **type**
- **Subnet** ID
- If it should have a **public IP** assigned (yes/no)
- **Security group** name
- **Key** name

```
python3 instance_launcher.py "<image_id> <instance_type> <subnet_id> <has_public_ip> <security_group_name> <key_name>"
```
**Example**:
```
python3 instance_launcher.py ami-096ccd3d4d0561c2e t2.micro subnet-06f709f8bc1cb17f6 yes http-ssh-sg CEU-Keys
```

### List instances
**Lists** all your **non-terminated** instances in your default region

```
python3 list-instances.py
```


### List subnets
**Lists** all the **subnets** instances of your default region

```
python3 list-subnets.py
```

### Ressource counter
**Lists** the number of following **ressources** created in your account

- **Volumes**
- **Snapshots**
- **Security Groups**
- **Load balancers**
- **Key Pairs**

```
python3 ressource-counter.py
```

### Instance Killer

**Terminates** the specified instance(s) (by providing its/their **instance ID**('s))

```
python3 instance_killer.py <instance1_id> <instance2_id> <instance3_id>..."
```
**Example**:
```
python3 instance-killer.py i-0c429c8738e9dc459
```

### Instance Tagger
**Assigns** a **tag** to a specific instance (by providing its **instance ID**)

```
python3 instance_tagger.py <instance_id> <tag_key> <tag_value>
```
**Example**:
```
python3 instance_tagger.py i-0c429c8738e9dc459 MyTagKey MyTagValue
```

### Instance Relauncher (by tag)
Finds all **stopped** instances (= **'stopped'** state name), and if it has the specified **Tag Key** it **launches the instance** again (= **'running'** state name)
```
python3 instance-relauncher-by-tag.py <tag_key>
```
**Example**:
```
python3 instance-relauncher-by-tag.py MyTagKey
```