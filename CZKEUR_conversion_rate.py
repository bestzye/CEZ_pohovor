import datetime #time stamp
import time #function sleep
import pandas as pd #pandas data analysis, csv 
from yahoofinancials import YahooFinancials #info from Yahoo!Finance

ticker = "EURCZK=X"
csv_name = "EURCZK_conversion_rate.csv"
yahoo_currency_rate = YahooFinancials(ticker)

def time_stamp():
    '''creates a time stamp (UTC time) as DD/MM/YYYY HH:MM:SS format'''
    return(datetime.datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S"))  

def get_EURCZK(ticker):
    '''creates first row with headers and time_stamp as index into new csv file'''
    data = pd.DataFrame({"current_rate": yahoo_currency_rate.get_current_price(), "current_change": yahoo_currency_rate.get_current_change(), "current_change[%]": (yahoo_currency_rate.get_current_percent_change()*100)}, index = [time_stamp()])
    data.to_csv(csv_name)
    
def insert_row():
    '''inserts new row into already existing csv file'''
    data2 = pd.DataFrame([[yahoo_currency_rate.get_current_price(), yahoo_currency_rate.get_current_change(), (yahoo_currency_rate.get_current_percent_change()*100)]],index = [time_stamp()])
    with open(csv_name, mode = 'a', newline='') as f:
        data2.to_csv(f, header = False)
        
get_EURCZK(ticker)
time.sleep(3600.0)
while True:
    insert_row()
    time.sleep(3600.0)