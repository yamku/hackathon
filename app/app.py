import boto3
import db
from flask import Flask, render_template

vpc_client = boto3.resource('ec2')
ddb = boto3.resource('dynamodb')

app = Flask(__name__) 
# app = Flask(__name__,static_folder="static", static_url_path="/")


@app.route('/')
def main():
    print(db.get_ec2_eni())
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
