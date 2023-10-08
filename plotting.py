###
###
### plotting.py - This script takes 'forecast.csv' as input which consists of columns:
### year,doy,h,m,magnitude,forecast
### respectively and creates a plot on Kp scale.
###
###

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('forecast.csv')
x = []
for i in data.index:
    x.append(int(data['year'][i])*525949 + int(data['doy'][i])*1440 + int(data['h'][i])*60 + int(data['m'][i]))
plt.plot(x,data['magnitude'],linewidth=1)
plt.yticks([0,1,4,6,8,12,15,20,29],[1,2,3,4,5,6,7,8,9])
plt.show()
