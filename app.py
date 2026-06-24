import requests

class SecEdgar:
    def __init__(self, fileurl):
        self.fileurl = fileurl
        self.namedict = {}
        self.tickerdict = {}

        headers = {'user-agent': 'MLT dennis7ni@gmail.com'}
        r = requests.get(self.fileurl, headers=headers)
        self.filejson = r.json()
        #print(r.text)
        #print(self.filejson)

        self.clk_json_to_dict()

    def clk_json_to_dict(self):
        self.namedict = {}
        self.tickerdict = {}
        for item in self.filejson.values():
            cik = str(item['cik_str']).zfill(10)
            name = item['title']
            ticker = item['ticker']

            self.namedict[name] = cik
            self.tickerdict[ticker] = cik
    
    def print_entry_name(self, name):
        cik = self.namedict.get(name)
        ticker = [k for k, v in self.tickerdict.items() if v == cik]
        print(f"Name: {name}, CIK: {cik}, Ticker: {ticker[0] if ticker else 'N/A'}")



    def print_entry_ticker(self, ticker):
        cik = self.tickerdict.get(ticker)
        name = [k for k, v in self.namedict.items() if v == cik]
        print(f"Ticker: {ticker}, CIK: {cik}, Name: {name[0] if name else 'N/A'}")
        

sec = SecEdgar("https://www.sec.gov/files/company_tickers.json") 
print(sec.print_entry_name("Apple Inc."))     # Example name for Apple Inc.
print(sec.print_entry_ticker("AAPL"))       # Example ticker for Apple Inc.