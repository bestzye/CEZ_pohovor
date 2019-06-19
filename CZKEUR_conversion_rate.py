import datetime #knihovna pro datum a čas (time stamp)
import time #knihovna pro 
import pandas as pd #knihovna pro analýzu dat pandas
from yahoofinancials import YahooFinancials #knihovna pro stahování informací z Yahoo!Finance

ticker = "EURCZK=X"
csv_name = "CZKEUR_conversion_rate.csv"
yahoo_currency_rate = YahooFinancials(ticker)

def time_stamp():
    return(datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")) #funkce na vytvoření time_stamp (UTC) ve formátu DD/MM/YYYY HH:MM:SS 
	
def get_CZKEUR(ticker):
    data = pd.DataFrame({"current_rate": yahoo_currency_rate.get_current_price(), "current_change": yahoo_currency_rate.get_current_change(), "current_change[%]": (yahoo_currency_rate.get_current_percent_change()*100)}, index = [time_stamp()])
    data.to_csv(csv_name)
	
def insert_row():
	data2 = pd.DataFrame([[yahoo_currency_rate.get_current_price(), yahoo_currency_rate.get_current_change(), (yahoo_currency_rate.get_current_percent_change()*100)]],index = [time_stamp()])
    with open(csv_name, mode = 'a', newline='') as f:
        data2.to_csv(f, header = False)
		
get_CZKEUR(ticker)
time.sleep(3600.0)
while True:
    insert_row()
    time.sleep(3600.0)
	