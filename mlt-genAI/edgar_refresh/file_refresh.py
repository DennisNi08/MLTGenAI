import json
import requests
import boto3
from secEdgar import SecEdgar



def lambda_handler(event, context):
    sec = SecEdgar("https://www.sec.gov/files/company_tickers.json")
    s3 = boto3.client('s3')
    response = requests.get("https://www.sec.gov/files/company_tickers.json", headers={'user-agent': 'MLT dennis7ni@gmail.com'})
    s3.put_object(Bucket='mlt-genai', Key='company_tickers.json', Body=response.content)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "file was uploaded successfully",
            # "location": ip.text.replace("\n", "")
        }),
    }
