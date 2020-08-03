import yfinance as yf

print('-- Stock Data Getter --')

# Gather User input
ticker = input("> Enter Stock Ticker Symbol: ")
period = input("> Enter Period [1day, 1mo, max]: ")

# Get Stock Data
stock = yf.Ticker(ticker).history(period)

print("-----------------------------------------")
print(stock)

# Save to csv
save = input("> Save as csv? [y, n]: ")

if save == 'y':
    stock.to_csv("{}.csv".format(ticker))
