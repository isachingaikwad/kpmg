import sys

try:
    from collections.abc import Mapping
except ImportError:
    from collections import Mapping

import boto3

def get_metadata(instance_ids, filter_name, filter_value ):
    """
    Returns the instance discription
    """
    try:
        response = ec2.describe_instances(
            Filters=[
                {
                    'Name': filter_name,
                    'Values': [
                    filter_value,
                    ]
                },
            ],
            InstanceIds=[
                instance_ids,
            ],
            DryRun=False
        )
    except Exception as e:
        print("Invalid Parameters")
        raise
    else:
        return response    

if __name__=='__main__': 

    ec2 = boto3.client('ec2')
    # Take user input instance_ids, filter_name, filter_value
    instance_ids = sys.argv[1]
    search_value = sys.argv[2]
    filter_name = 'instance-type'
    filter_value = 't2.micro'
    result = get_metadata(instance_ids, filter_name, filter_value)
    print(result['Reservations'][0]['Instances'][0][search_value])

    # You can filterable instance data using below supported values
    """
    'AmiLaunchIndex',
    'ImageId', 
    'InstanceId', 
    'InstanceType', 
    'KeyName', 
    'LaunchTime', 
    'Monitoring', 
    'Placement', 
    'PrivateDnsName', 
    'PrivateIpAddress', 
    'ProductCodes', 
    'PublicDnsName', 
    'PublicIpAddress', 
    'State', 
    'StateTransitionReason', 
    'SubnetId', 
    'VpcId', 
    'Architecture', 
    'BlockDeviceMappings',
    'ClientToken', 
    'EbsOptimized', 
    'EnaSupport', 
    'Hypervisor', 
    'NetworkInterfaces', 
    'RootDeviceName', 
    'RootDeviceType', 
    'SecurityGroups', 
    'SourceDestCheck',
    'Tags', 
    'VirtualizationType', 
    'CpuOptions', 
    'CapacityReservationSpecification', 
    'HibernationOptions', 
    'MetadataOptions', 
    'EnclaveOptions', 
    'PlatformDetails', 
    'UsageOperation', 
    'UsageOperationUpdateTime', 
    'PrivateDnsNameOptions', 
    'MaintenanceOptions'
    """
    # Sample running command
    # python get_metadata.py 'i-009f2411dbc169d70' 'InstanceType'

