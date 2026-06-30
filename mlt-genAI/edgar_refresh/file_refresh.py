import json
import requests
import boto3
import os

BUCKET_NAME = os.environ['BUCKET_NAME']

def lambda_handler(event, context):
    url = "https://www.sec.gov/files/company_tickers.json"
    response = requests.get("https://www.sec.gov/files/company_tickers.json", headers={'user-agent': 'MLT dennis7ni@gmail.com'})
    response.raise_for_status() 

    s3 = boto3.client('s3')
    s3.put_object(Bucket=BUCKET_NAME, Key='company_tickers.json', Body=response.content)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "file was uploaded successfully",
            # "location": ip.text.replace("\n", "")
        }),
    }
