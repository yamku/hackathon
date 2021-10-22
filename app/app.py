import boto3
import db
from flask import Flask, render_template
from json import dumps
vpc_client = boto3.resource('ec2')
ddb = boto3.resource('dynamodb')

app = Flask(__name__) 
# app = Flask(__name__,static_folder="static", static_url_path="/")


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
