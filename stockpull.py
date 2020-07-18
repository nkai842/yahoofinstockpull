
from YahooFin import DataYahoo
import pandas as pd


ticker = ['CROX','AAPL','AIG','BYND',
'ROKU','CPB']

# sets "t" as YahooFin module

t = DataYahoo(ticker)

## Calls pull_data() method from YahooFin

po = t.pull_data()

## Creates a data frame and prints
df = pd.DataFrame(po)
print(df)

## Imports data frame to csv file to then manipulate in excel
df.to_csv('stocks.csv', index = True)
