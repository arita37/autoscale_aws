import requests

def lambda_handler(event, context):
    r = requests.get('https://boto3.amazonaws.com/')
    return r.status_code
