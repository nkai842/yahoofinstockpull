
from YahooFin import DataYahoo
import pandas as pd

ticker = ['CROX','AAPL','AIG','BYND',
'ROKU','CPB']

t = DataYahoo(ticker)
po = t.pull_data()

df = pd.DataFrame(po)
print(df)
df.to_csv('stocks.csv', index = True)
