from urllib import request

goog_url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1654329299&period2=1685865299&interval=1d&events=history&includeAdjustedClose=true'

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'/Users/peterszasz/Desktop/Python tutorial/goog.csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")


download_stock_data(goog_url)