import datetime #datum a cas (time stamp)
import time #knihovna s funkci sleep
import pandas as pd #analyza dat pandas
from yahoofinancials import YahooFinancials #stahovani informaci z Yahoo!Finance

ticker = "EURCZK=X"
csv_name = "EURCZK_conversion_rate.csv"
yahoo_currency_rate = YahooFinancials(ticker)

def time_stamp():
    '''vytvori time_stamp (UTC) ve formatu DD/MM/YYYY HH:MM:SS'''
    return(datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S"))  
	
def get_EURCZK(ticker):
	'''vytvori prvni radek v csv vcetne nazvu sloupcu, indexem je time_stamp, ulozi nove csv'''
	data = pd.DataFrame({"current_rate": yahoo_currency_rate.get_current_price(), "current_change": yahoo_currency_rate.get_current_change(), "current_change[%]": (yahoo_currency_rate.get_current_percent_change()*100)}, index = [time_stamp()])
	data.to_csv(csv_name)
	
def insert_row():
	'''prida radek v jiz existujicim csv'''
	data2 = pd.DataFrame([[yahoo_currency_rate.get_current_price(), yahoo_currency_rate.get_current_change(), (yahoo_currency_rate.get_current_percent_change()*100)]],index = [time_stamp()])
	with open(csv_name, mode = 'a', newline='') as f:
		data2.to_csv(f, header = False)
		
get_EURCZK(ticker)
time.sleep(3600.0)
while True:
    insert_row()
    time.sleep(3600.0)