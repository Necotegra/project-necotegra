###
###
### detect.py - This script takes 'hour_data.csv' as input which consists of columns:
### "year","doy","h","m","velocity","density","temperature","minutes"
### respectivelty.
###
###

import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler

model = tf.keras.models.load_model("model.h5")

new_data = pd.read_csv('hour_data.csv')
original = pd.read_csv('hour_data.csv')

new_data = new_data.drop(columns=['year','doy','h','m','minutes'])
scaler = StandardScaler()
new_data = scaler.fit_transform(new_data)

predictions = model.predict(new_data)
predictions_df = pd.DataFrame(predictions, columns=['magnitude'])

result = pd.concat([original,predictions_df],axis=1)
result.to_csv("result.csv", index=False)
