from iexfinance.stocks import Stock
import pandas as pd

sharecode = input('Enter a valid ticker symbol: ')
stock = Stock(sharecode)

dailydiff = float(((float(stock.get_close()))-(float(stock.get_open()))))
dailydiff = "%0.2f"%dailydiff

percent_change = float((float(dailydiff))/(float(stock.get_open())))*100

sheet = {'Open Price':[stock.get_open()],
         'Current Price':[stock.get_price()],
         'Close Price':[stock.get_close()],
         'Change in Price':[dailydiff],
         'Percent Change':[percent_change]}

pd.set_option('display.max_columns',None)
df = pd.DataFrame(sheet)

print(df)


