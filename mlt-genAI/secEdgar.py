import requests
from bs4 import BeautifulSoup

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

    def annual_filing(self, cik,year):
        url = f"https://data.sec.gov/submissions/CIK{cik}.json"
        headers = {'user-agent': 'MLT dennis7ni@gmail.com'}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            data = r.json()
            filings = data.get('filings', {}).get('recent', {})
            for i in range(len(filings.get('accessionNumber', []))):
                filing_year = filings.get('filingDate', [])[i][:4]
                form_type = filings.get('form', [])[i]
                if filing_year == str(year) and form_type == '10-K':
                    accession_number = filings.get('accessionNumber', [])[i]
                    form_type = filings.get('form', [])[i]
                    document_name = filings.get('primaryDocument', [])[i]
                    filing_date = filings.get('filingDate', [])[i]
                    print(self.get_forms(cik, accession_number, document_name))
        

    def get_forms(self, cik, accession_number, document_name):
        accession_id = accession_number.replace('-', '')
        if not document_name:
            document_name = 'index.html'
        url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession_id}/{document_name}"
        headers = {'user-agent': 'MLT dennis7ni@gmail.com'}
        r = requests.get(url, headers=headers)

        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'html.parser')
        
            for tag in soup(['script', 'style']):
                tag.decompose()
            
            text = soup.get_text(separator='\n', strip=True)
            return text
        else:
            print(f"Error fetching form: {r.status_code} -> {url}")
            return None
        
    def quarterly_filing(self, cik, year, quarter):
        url = f"https://data.sec.gov/submissions/CIK{cik}.json"
        headers = {'user-agent': 'MLT dennis7ni@gmail.com'}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            data = r.json()
            filings = data.get('filings', {}).get('recent', {})
            for i in range(len(filings.get('accessionNumber', []))):
                filing_year = filings.get('filingDate', [])[i][:4]
                filing_month = int(filings.get('filingDate', [])[i][5:7])
                filing_quarter = (filing_month - 1) // 3 + 1
                if filing_year == str(year) and filing_quarter == quarter:
                    accession_number = filings.get('accessionNumber', [])[i]
                    document_name = filings.get('primaryDocument', [])[i]
                    filing_date = filings.get('filingDate', [])[i]
                    print(self.get_forms(cik, accession_number, document_name))

    


sec = SecEdgar("https://www.sec.gov/files/company_tickers.json") 
#print(sec.print_entry_name("Apple Inc."))     # Example name for Apple Inc.
#print(sec.print_entry_ticker("AAPL"))       # Example ticker for Apple Inc.
#print(sec.annual_filing("0000320193", 2022))  # Example CIK for Apple Inc. and year 2022
#print(sec.quarterly_filing("0000320193", 2022, 1))  # Example CIK for Apple Inc., year 2022, and quarter 1

