import pandas as pd 
import numpy as np
import openpyxl

def load_house_price_and_earning_by_district():
    workbook = openpyxl.load_workbook('Data/England_house_price_and_earning_statistics.xlsx')

    median_house_price = workbook['5a']
    median_house_price = pd.DataFrame(median_house_price.values)
    median_house_price = median_house_price.drop(labels=range(0,6), axis=0)
    median_house_price.columns = list(median_house_price.loc[6,:])
    median_house_price = median_house_price.drop(labels=6, axis=0)
    median_house_price = median_house_price.drop(labels=[343, 344, 345, 346, 347, 348, 349], axis=0)
    median_house_price = median_house_price.drop(labels=list(median_house_price[median_house_price['Region name']=='Wales'].index), axis=0)
    median_house_price.index = range(0,len(median_house_price.index))
    
    lower_quatile_house_price = workbook['6a']
    lower_quatile_house_price = pd.DataFrame(lower_quatile_house_price.values)
    lower_quatile_house_price = lower_quatile_house_price.drop(labels=range(0,6), axis=0)
    lower_quatile_house_price.columns = list(lower_quatile_house_price.loc[6,:])
    lower_quatile_house_price = lower_quatile_house_price.drop(labels=6, axis=0)
    lower_quatile_house_price = lower_quatile_house_price.drop(labels=[343, 344, 345, 346, 347, 348, 349], axis=0)
    lower_quatile_house_price = lower_quatile_house_price.drop(labels=list(lower_quatile_house_price[lower_quatile_house_price['Region name']=='Wales'].index), axis=0)
    lower_quatile_house_price.index = range(0,len(lower_quatile_house_price.index))
    
    median_earning = workbook['5b']
    median_earning = pd.DataFrame(median_earning.values)
    median_earning = median_earning.drop(labels=range(0,6), axis=0)
    median_earning.columns = list(median_earning.loc[6,:])
    median_earning = median_earning.drop(labels=6, axis=0)
    median_earning = median_earning.drop(labels=[343, 344, 345, 346, 347, 348, 349, 350, 351, 352], axis=0)
    median_earning = median_earning.drop(labels=list(median_earning[median_earning['Region name']=='Wales'].index), axis=0)
    median_earning = median_earning.drop(labels=[median_earning.columns[23],median_earning.columns[24]], axis=1)
    median_earning.index = range(0,len(median_earning.index))

    lower_quatile_earning = workbook['6b']
    lower_quatile_earning = pd.DataFrame(lower_quatile_earning.values)
    lower_quatile_earning = lower_quatile_earning.drop(labels=range(0,6), axis=0)
    lower_quatile_earning.columns = list(lower_quatile_earning.loc[6,:])
    lower_quatile_earning = lower_quatile_earning.drop(labels=6, axis=0)
    lower_quatile_earning = lower_quatile_earning.drop(labels=[343, 344, 345, 346, 347, 348, 349, 350, 351, 352], axis=0)
    lower_quatile_earning = lower_quatile_earning.drop(labels=list(lower_quatile_earning[lower_quatile_earning['Region name']=='Wales'].index), axis=0)
    lower_quatile_earning = lower_quatile_earning.drop(labels=[lower_quatile_earning.columns[23],lower_quatile_earning.columns[24]], axis=1)
    lower_quatile_earning.index = range(0,len(lower_quatile_earning.index))
    
    lower_quatile_house_price.columns = list(median_earning.columns)
    median_house_price.columns = list(median_earning.columns)
    
    return median_house_price,lower_quatile_house_price,median_earning,lower_quatile_earning

