###
###
### classify.py - This script takes 'report.csv' as input which consists of columns:
### "year","doy","h","m","magnitude"
### respectively and labels each row on Kp scale.
###
###

import pandas as pd

predictions = pd.read_csv('report.csv')
classes=[]

for i in predictions.index:
    magnitude = float(predictions['magnitude'][i])
    if magnitude < 1:
        classes.append(1)
    elif magnitude < 4:
        classes.append(2)
    elif magnitude < 6:
        classes.append(3)
    elif magnitude < 8:
        classes.append(4)
    elif magnitude < 12:
        classes.append(5)
    elif magnitude < 15:
        classes.append(6)
    elif magnitude < 20:
        classes.append(7)
    elif magnitude < 29:
        classes.append(8)
    else:
        classes.append(9)

predictions = predictions.assign(forecast=classes)
print(predictions)
predictions.to_csv('forecast.csv',index=False)
