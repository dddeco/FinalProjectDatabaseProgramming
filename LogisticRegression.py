import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings

warnings.filterwarnings(action='ignore')
url = 'heart.csv'
df = pd.read_csv(url)

x = df[df.columns[0:13]]
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)

model = LogisticRegression()
model.fit(X_train,y_train)

dataframe_pred = pd.read_csv('heart_pred.csv')
X_pred = dataframe_pred[dataframe_pred.columns[0:13]]
tuples = [tuple(x) for x in X_pred.values]
pred_label = []
for input in tuples:
    input_array = np.asarray(input)
    input_reshape = input_array.reshape(1, -1)
    prediction = model.predict(input_reshape)
    pred_label.append(prediction[0])


dataframe_pred.insert(13,'target',value = pred_label)
dataframe_pred.to_csv('Pred.csv',index=False)

