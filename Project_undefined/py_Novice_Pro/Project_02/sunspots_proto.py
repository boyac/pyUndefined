from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF

#URL = 'ftp://ftp.swpc.noaa.gov/pub/weekly/Predict.txt'
"""
# YR MO   PREDICTED    HIGH    LOW   PREDICTED    HIGH    LOW
#--------------------------------------------------------------
2015 09        40.2    41.2    39.2      111.3   112.3   110.3
2015 10        40.9    42.9    38.9      109.2   110.2   108.2
2015 11        40.6    43.6    37.6      107.3   109.3   105.3
2015 12        40.5    45.5    35.5      105.4   108.4   102.4
2016 01        40.7    45.7    35.7      104.0   108.0   100.0
2016 02        40.9    46.9    34.9      103.1   107.1    99.1
2016 03        40.6    47.6    33.6      102.4   107.4    97.4
2016 04        40.3    47.3    33.3      101.6   107.6    95.6
2016 05        40.2    48.2    32.2      100.4   107.4    93.4
2016 06        40.1    49.1    31.1       98.7   106.7    90.7
2016 07        40.0    49.0    31.0       97.1   105.1    89.1
2016 08        39.9    49.9    29.9       95.8   104.8    86.8
2016 09        39.0    49.0    29.0       94.5   103.5    85.5
2016 10        37.3    47.3    27.3       92.9   101.9    83.9
"""
data = [
# Year Month Predicted High Low
(2015, 9, 40.2, 41.2, 39.2),
(2015, 10, 40.9, 42.9, 38.9),
(2015, 11, 40.6, 43.6, 37.6),
(2015, 12, 40.5, 45.5, 35.5),
(2016, 1, 40.7, 45.7, 35.7),
(2016, 2, 40.9, 46.9, 34.9),
(2016, 3, 40.6, 47.6, 33.6),
(2016, 4, 40.3, 47.3, 33.3),
(2016, 5, 40.2, 48.2, 32.2),
(2016, 6, 40.1, 49.1, 31.1),
]

drawing = Drawing(200, 150)

pred = [row[2]-4 for row in data]
high = [row[3]-4 for row in data]
low = [row[4]-4 for row in data]
times = [200*((row[0] + row[1]/12.0) - 2015)-110 for row in data]

drawing.add(PolyLine(zip(times, pred), strokeColor=colors.blue))
drawing.add(PolyLine(zip(times, high), strokeColor=colors.red))
drawing.add(PolyLine(zip(times, low), strokeColor=colors.green))
drawing.add(String(65, 115, 'Sunspots', fontSize=18, fileColor=colors.red))

renderPDF.drawToFile(drawing, 'report1.pdf', 'Sunspots')
