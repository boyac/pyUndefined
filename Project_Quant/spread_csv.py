# Calculate spread of stock price (High substract Low) and write into a new CSV
# Data from Quandl: https://www.quandl.com/data/XJPX/1319-Nomura-Asset-Management-Co-Ltd-1319-Adjusted-Stock-Prices
# 1319 | Nomura Nikkei 300 Listed ETF

import csv

with open('nomura_1319.csv', 'rb') as old_csv: # Using Nomura_1319 as sample data
    csv_reader = csv.reader(old_csv)
    with open('nomura_1319.csv_new.csv', 'wb') as new_csv:
        csv_writer = csv.writer(new_csv)
        for i, row in enumerate(csv_reader):
            if i != 0:
                row.append(float(row[2]) - float(row[3]))
                csv_writer.writerow(row)
