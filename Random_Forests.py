import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# load data
df = pd.read_csv('Household Adjusted Normalised Combined Ages.csv')

features = df

all_features = []

rem_features = ['NUTS_ID','NUTS Name','Live Births','Deaths','Population',
'Births From Mother Aged 25-29','Births From Mother Aged 30-34','Net Migration 2018','Employment (%)','Order/household']

relevant_features = ['New residents',
'Births From Mother Aged 20-24','Births From Mother Aged 35+','GDP (million USD)',
'Population Density']


for feature in rem_features:
    features = features.drop(feature, 1)

features = features.drop(relevant_features[0], 1)


labels = df['Order/household'].to_numpy()
features = features.to_numpy()


# split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.25, random_state=6)

model_rf = RandomForestRegressor(n_estimators=500, oob_score=True, random_state=100)
model_rf.fit(X_train, y_train)
estimators = model_rf.estimators_

def predict(w, i):
    model_rf.estimators_ = estimators[0:i+1]
    return model_rf.predict(X_train)


pred_train_rf = model_rf.predict(X_train)
training_error = (np.sqrt(mean_squared_error(y_train, pred_train_rf)))
training_acc = (r2_score(y_train, pred_train_rf))*100

pred_test_rf = model_rf.predict(X_test)
testing_error = (np.sqrt(mean_squared_error(y_test, pred_test_rf)))
testing_acc = (r2_score(y_test, pred_test_rf))*100

# for i in range(0, len(y_test)-1):
#     #print('Actual: ' + str(y_test[i]) + ' | Prediction: ' + str(pred_test_rf[i]))
#     print(str(y_test[i]) + "," + str(pred_test_rf[i]))
# print(testing_acc)

print(predict(X_test,4))


