import requests

class SecEdgar:
    def __init__(self, fileurl):
        self.fileurl = fileurl
        self.namedict = {}
        self.tickerdict = {}

        headers = {'user-agent': 'MLT dennis7ni@gmail.com'}
        r = requests.get(self.fileurl, headers=headers)

        print(r.text)
        print(self.filejson)

        self.clk_json_to_dict()

    def clk_json_to_dict(self):
        self.namedict = {}
        self.tickerdict = {}

se = SecEdgar("https://www.sec.gov/files/company_tickers.json") 