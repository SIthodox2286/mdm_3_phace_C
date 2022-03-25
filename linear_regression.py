import numpy as np
import pandas as pd
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score


def produce_predictions_linear_regression(train_X, test_X, train_y):
    # function to find predictions using LinearRegression model from sklearn

    model = LinearRegression()
    model.fit(train_X, train_y)
    predictions = model.predict(test_X)

    return predictions


df = pd.read_csv('Non-Household Adjusted No Zero.csv')

features = df

rem_features = ['Household', 'Orders', 'NUTS Name', 'NUTS ID', 'Country ', 'Country Code', 'NUTS LEVEL',
                'Births From Mother Aged 20-24', 'Births From Mother Aged 25-29', 'Births From Mother Aged 30-34',
                'Births From Mother Aged 40-44', 'Births From Mother Aged 45+',
                'New residents in the region coming from another region of the same country', 'Order/household']

for feature in rem_features:
    features = features.drop(feature, 1)

labels = df['Orders']

features = features.to_numpy()
labels = labels.to_numpy()


train_X, test_X, train_y, test_y = train_test_split(features, labels, test_size=0.27, random_state=0)
predictions = produce_predictions_linear_regression(train_X, test_X, train_y)
score = r2_score(test_y, predictions)

for i in range(0, len(test_y)-1):
    print('Actual: ' + str(test_y[i]) + ' | Prediction: ' + str(predictions[i]))
print(score*100)
