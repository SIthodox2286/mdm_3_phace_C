import pandas as pd
import sys
import os
import openpyxl

def load_data(path,sheet ,data_extract ,model, column):
    df =pd.read_excel(path, sheet_name=sheet)
    df = df.sort_values(by='Local Authority name', key=lambda x: x.str.len())
    df = df.reset_index(drop=True)
    k =len(list(df.index))
    #print( df['Local Authority name'][1] )
    model.insert(column , column=data_extract, value= None)
    for n in range(0, 347):
        loop(model , df, data_extract ,n ,k)
    #print(model)
    column+=1
    return model , column



def loop(model , df, data_extract ,n ,k):
    for i in range(0,k):
        if model.values[n][0] == df['Local Authority code'][i] or str.lower(model.values[n][1]) in str.lower(df['Local Authority name'][i] ):
            model.at[n,data_extract] = df[data_extract][i]
            df.at[i,'Local Authority code'] = -999
            df.at[i,'Local Authority name'] = 'NaN'
            df = pd.DataFrame(data = df)
            return df

            break