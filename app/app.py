import boto3
import db
from json import dumps

#print(vpns)
# response =  [
#     db.get_ec2_eni(),
#     db.get_nacl(),
#     db.get_route_tables(),
#     db.get_security_groups(),
#     db.get_vpn()
# ]

response_dict = {
    "enis": db.get_ec2_eni(),
    "nacls": db.get_nacl(),
    "route_tables": db.get_route_tables(),
    "security_groups": db.get_security_groups(),
    "vpns": db.get_vpn()
}

def main():

    return dumps(response_dict)

if __name__ == '__main__':
    print(main())
