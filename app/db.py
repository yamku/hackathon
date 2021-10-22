from botocore.config import Config
import boto3
from json import dumps,loads
from pyvis.network import Network
import pandas as pd
import sys


my_config = Config(
    region_name = 'ap-southeast-2',
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)

vpc_client = boto3.client('ec2', config = my_config)
ddb = boto3.resource('dynamodb')
net = Network(notebook=True)

eni = {}
vpns = {}

def get_ec2_eni():
    try:
        for network_interface in vpc_client.describe_network_interfaces()["NetworkInterfaces"]:
            # print(eni)
            # eni.append({
            #     "AvailabilityZone": network_interface["AvailabilityZone"],
            #     "Description": network_interface["Description"],
            # })
            eni[network_interface["PrivateIpAddress"]] = {
                "AvailabilityZone": network_interface["AvailabilityZone"],
                "Description": network_interface["Description"]
            }
        
    except:
        print("Exception Occured at get_ec2_eni")

#print(dumps(get_ec2_eni(), indent=4, sort_keys=True))

    return eni
def get_vpn():
    try:
        for vpn_gateway in vpc_client.describe_vpn_gateways()["VpnGateways"]:
            vpns[vpn_gateway["VpnGatewayId"]] = {
                "AvailabilityZone" : vpn_gateway["AvailabilityZone"],
                "VpcAttachments" : vpn_gateway["VpcAttachments"]
            }
    except:
        print("Exception Occured get_vpn()")

    return vpns

#def get_tgw():
#    try:
#        for tgw in vpc_client.describe

# print(dumps(get_vpn(), indent=4, sort_keys=True))
data = dumps(get_ec2_eni(), indent=4, sort_keys=True)

if __name__ == "__main__":
   print(data)




