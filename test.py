import pandas as pd
import sys
import os

def load_data(path,data_extract,model):
    df =pd.read_csv(path)
    print(df)
    print( df['Local Authority code'][1] )
    model.insert(2, column=data_extract, value= None)
    for n in range(0, 346):
        loop(model , df, data_extract ,n)


    print(model)

def loop(model , df, data_extract ,n):
    for i in range(0,429):
        if model.values[n][0] == df['Local Authority code'][i]:

            model.at[n,data_extract] = df[data_extract][i]

            break

    return n
    print(model)




model = pd.read_csv('test.csv')

print(model.values[0][0])
load_data('Number_of_Schools_UK.csv','Violence with injury',model)