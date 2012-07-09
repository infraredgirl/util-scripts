import time
import boto.ec2
from aws_settings import *



def connect_to_ec2():
    """
    Creates and returns a connection object to EC2.
    """
    print 'Connecting to region %s with access key id = %s and secret access key = %s ...' % (REGION,
                                                                                              AWS_ACCESS_KEY_ID,
                                                                                              AWS_SECRET_ACCESS_KEY)
    connection = boto.ec2.connect_to_region(
        region_name = REGION,
        aws_access_key_id = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
    )

    print 'Connected.'
    return connection


def get_non_production_instances(connection):
    """
    Returns a list of non-production instances.
    """
    print 'Getting non-production instances ...'
    reservations = connection.get_all_instances()
    instances = [i for r in reservations for i in r.instances]
    instances = filter(lambda i: i.tags.get(PROD_INSTANCE_TAG_KEY)!=PROD_INSTANCE_TAG_VALUE, instances)

    print 'Found %d instances.' % len(instances)
    return instances


def stop_non_production_instances():
    """
    Stops all non-production instances.
    """
    connection = connect_to_ec2()
    instances = get_non_production_instances(connection)

    print 'Stopping %d non-production instances ...' % len(instances)

    for instance in instances:
        instance.stop()
        print '\tInstance %s stopped.' % instance.id

    print 'Done stopping instances.'


def start_non_production_instances():
    """
    Starts all stopped non-production instances and associates their respective elastic IPs.
    """
    connection = connect_to_ec2()
    instances = get_non_production_instances(connection)

    print 'Starting %d non-production instances ...' % len(instances)

    for instance in instances:
        if instance.state == 'stopped':
            instance.start()
            print '\tInstance %s %s.' % (instance.id, instance.state)

            while instance.state != 'running':
                time.sleep(5)
                instance.update()
                print '\tInstance %s %s.' % (instance.id, instance.state)

            ip = ELASTIC_IPS.get(instance.id)

            if ip:
                connection.associate_address(instance.id, ip)
                print '\tInstance %s associated to elastic ip %s.' % (instance.id, ip)

    print 'Done starting instances.'
