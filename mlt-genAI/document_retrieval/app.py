import json
from secEdgar import SecEdgar



def lambda_handler(event, context):
    user_request = json.loads(event['body'])

    sec = SecEdgar("https://www.sec.gov/files/company_tickers.json")

    cik = sec.tickerdict.get(user_request['ticker'])
    year = user_request['year']
    form_type = user_request['form_type']

    if form_type[0] == "Q":
        sec.quarterly_filing(cik, year, form_type)
    elif form_type == "FY":
        sec.annual_filing(cik, year)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "file was uploaded successfully",
            # "location": ip.text.replace("\n", "")
        }),
    }
