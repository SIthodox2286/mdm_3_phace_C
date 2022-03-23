import pandas as pd 
import numpy as np
import openpyxl

def load_house_price_and_earning_by_district():
    workbook = openpyxl.load_workbook('Data/ERIC/England_house_price_and_earning_statistics.xlsx')

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
    
    median_quatile_ratio = workbook['5c']
    median_quatile_ratio = pd.DataFrame(median_quatile_ratio.values)
    median_quatile_ratio = median_quatile_ratio.drop(labels=range(0,6), axis=0)
    median_quatile_ratio.columns = list(median_quatile_ratio.loc[6,:])
    median_quatile_ratio = median_quatile_ratio.drop(labels=6, axis=0)
    median_quatile_ratio = median_quatile_ratio.drop(labels=median_quatile_ratio.loc[range(343,356),:].index, axis=0)
    median_quatile_ratio = median_quatile_ratio.drop(labels=median_quatile_ratio.loc[:,:].columns[range(23,42)], axis=1)
    median_quatile_ratio = median_quatile_ratio.drop(labels=list(median_quatile_ratio[median_quatile_ratio['Region name']=='Wales'].index), axis=0)
    median_quatile_ratio.index = range(0,len(median_quatile_ratio.index))
    
    lower_quatile_ratio = workbook['6c']
    lower_quatile_ratio = pd.DataFrame(lower_quatile_ratio.values)
    lower_quatile_ratio = lower_quatile_ratio.drop(labels=range(0,6), axis=0)
    lower_quatile_ratio.columns = list(lower_quatile_ratio.loc[6,:])
    lower_quatile_ratio = lower_quatile_ratio.drop(labels=6, axis=0)
    lower_quatile_ratio = lower_quatile_ratio.drop(labels=lower_quatile_ratio.iloc[range(336,349),:].index, axis=0)
    lower_quatile_ratio = lower_quatile_ratio.drop(labels=lower_quatile_ratio.loc[:,:].columns[range(23,42)], axis=1)
    lower_quatile_ratio = lower_quatile_ratio.drop(labels=list(lower_quatile_earning[lower_quatile_earning['Region name']=='Wales'].index), axis=0)
    lower_quatile_ratio.index = range(0,len(lower_quatile_ratio.index))
    
    lower_quatile_house_price.columns = list(median_earning.columns)
    median_house_price.columns = list(median_earning.columns)
    
    return median_house_price,lower_quatile_house_price,median_earning,lower_quatile_earning,median_quatile_ratio,lower_quatile_ratio

def load_council_tax_data():
    # Open the Council tax data set
    workbook = openpyxl.load_workbook('Data/ERIC/ENGLAND_council_tax_band_properties.xlsx')

    # read columns that contains the lastest property counts for all bands (2021's) and administrative area names in England.
    council_tax_band = workbook['CTSOP4.0']
    council_tax_band = pd.DataFrame(council_tax_band.values)
    council_tax_band = council_tax_band.drop(labels=range(0,5), axis=0)
    council_tax_band = council_tax_band.drop(columns=range(council_tax_band.columns[6],council_tax_band.columns[31]))
    council_tax_band = council_tax_band.drop(columns=range(council_tax_band.columns[0],council_tax_band.columns[3]))
    council_tax_band = pd.DataFrame(council_tax_band)
    council_tax_band = council_tax_band.rename(columns={3:'ecode',4:'area_name', 5:'band', 31:'number_of_properties'})

    # Extract the Area Name labels
    area_names = list(pd.unique(council_tax_band[:]['area_name']))
    ecode = list(pd.unique(council_tax_band[:]['ecode']))
    
    # Extract the properties in each band.
    band_A = council_tax_band[council_tax_band["band"]=='A'].replace('-', 0) # A, Up to and including £40,000, tax charge £1,486.91
    band_B = council_tax_band[council_tax_band["band"]=='B'].replace('-', 0) # B, £40,001 - £52,000, tax charge £1,734.73
    band_C = council_tax_band[council_tax_band["band"]=='C'].replace('-', 0) # C, £52,001 - £68,000, tax charge £1,982.55
    band_D = council_tax_band[council_tax_band["band"]=='D'].replace('-', 0) # D, £68,001 - £88,000, tax charge £2,230.37
    band_E = council_tax_band[council_tax_band["band"]=='E'].replace('-', 0) # E, £88,001 - £120,000, tax charge £2,726.01
    band_F = council_tax_band[council_tax_band["band"]=='F'].replace('-', 0) # F, £120,001 - £160,000, tax charge £3,221.64
    band_G = council_tax_band[council_tax_band["band"]=='G'].replace('-', 0) # G, £160,001 - £320,000, tax charge £3,717.28
    band_H = council_tax_band[council_tax_band["band"]=='H'].replace('-', 0) # H, Over £320,000, tax charge £4,460.74

    # Transform them into nd.array for vector sum purpose.
    band_A = np.array(band_A['number_of_properties']).reshape(-1,1)
    band_B = np.array(band_B['number_of_properties']).reshape(-1,1)
    band_C = np.array(band_C['number_of_properties']).reshape(-1,1)
    band_D = np.array(band_D['number_of_properties']).reshape(-1,1)
    band_E = np.array(band_E['number_of_properties']).reshape(-1,1)
    band_F = np.array(band_F['number_of_properties']).reshape(-1,1)
    band_G = np.array(band_G['number_of_properties']).reshape(-1,1)
    band_H = np.array(band_H['number_of_properties']).reshape(-1,1)
    
    # 8 groups are too many for analysis, thus put them into four groups, catergorized by their valuations.
    # 0 ~ 52k, approximately the houses that are around 50k, mostly small flats or less favoured housing;
    houses_above_0k = pd.DataFrame({'Local Authority code':list(ecode),'Local Authority name':list(area_names),'A_B_property_counts':list((band_A+band_B).reshape(1,-1)[0])})
    # 52 ~ 88k, around 100k, low-average standard;
    houses_above_52k = pd.DataFrame({'Local Authority code':list(ecode),'Local Authority name':area_names,'C_D_property_counts':list((band_C+band_D).reshape(1,-1)[0])})
    # 88k ~ 160k, from 100k to 150k, high-average standard;
    houses_above_88k = pd.DataFrame({'Local Authority code':list(ecode),'Local Authority name':area_names,'E_F_property_counts':list((band_E+band_F).reshape(1,-1)[0])})
    # 160k above, above 150k, more or less luxury houses;
    houses_above_160k = pd.DataFrame({'Local Authority code':list(ecode),'Local Authority name':area_names,'G_H_property_counts':list((band_G+band_H).reshape(1,-1)[0])})
    
    # A data set to combine all bands
    council_tax_band_all = pd.DataFrame({'Local Authority code':list(ecode),'area_names':list(area_names),'A':list(band_A),'B':list(band_B)
                                         ,'C':list(band_C),'D':list(band_D)
                                         ,'E':list(band_E),'F':list(band_F),
                                        'G':list(band_G),'H':list(band_H)})
    
    # Return the tables
    return houses_above_0k, houses_above_52k, houses_above_88k, houses_above_160k,council_tax_band_all

def load_homeless_demographic():
    workbook = pd.ExcelFile('Data/ERIC/England_HomelessData_until2020.xlsx')
    worksheet = workbook.parse(workbook.sheet_names[7])
    hl_demographic = worksheet.drop(labels=range(325,342), axis=0)
    hl_demographic = hl_demographic.drop(columns=hl_demographic.columns[range(11,60)])
    
    hl_demographic.iloc[1,[0]] = 'Code'
    hl_demographic.iloc[1,[1]] = 'Area_name'
    hl_demographic.columns = list(hl_demographic.iloc[1,:])
    hl_demographic = hl_demographic.drop(labels=range(0,16), axis=0)
    hl_demographic.index = range(0,len(hl_demographic.index))
    
    return hl_demographic

def load_processed_general_data():
    workbook = pd.ExcelFile('revised_all_in_one.xlsx')
    worksheet = workbook.parse(workbook.sheet_names[1])
    worksheet.index = list(range(0,len(list(worksheet['Numbering']))))
    worksheet = worksheet.drop(labels='Numbering',axis = 1)
    
    # Area Name
    local_authority_names = worksheet['Local Authority name']
    
    # Housing prices data in Pound Sterling;
    median_houses_2020 = worksheet['median_houses_2020']
    lower_quatile_houses_2020 = worksheet['lower_quatile_houses_2020']
    
    # Valuation of the Properties;
    A_B_property_counts = worksheet['A_B_property_counts'] 
    C_D_property_counts = worksheet['C_D_property_counts']
    E_F_property_counts = worksheet['E_F_property_counts']
    G_H_property_counts = worksheet['G_H_property_counts']
    
    return median_houses_2020,lower_quatile_houses_2020,A_B_property_counts,C_D_property_counts,E_F_property_counts,G_H_property_counts,local_authority_names

def load_processed_society_data():
    workbook = pd.ExcelFile('revised_all_in_one.xlsx')
    worksheet = workbook.parse(workbook.sheet_names[1])
    worksheet.index = list(range(0,len(list(worksheet['Numbering']))))
    worksheet = worksheet.drop(labels='Numbering',axis = 1)
    
    # Earning and Affordablity Ratio and rent:
    lower_quatile_earning_2020 = worksheet['lower_quatile_earning_2020']
    ratio_by_lower_quatile_2020 = worksheet['ratio_by_lower_quatile_2020']
    median_earning_2020 = worksheet['median_earning_2020']
    ratio_by_medians_2020 = worksheet['ratio_by_medians_2020']
    month_rent_higher_quatile = worksheet['Median']
    month_rent_lower_quatile = worksheet['Lower quartile']

    # Society issues;
    total_threaten_homeless = worksheet['Total_Threaten_or_is_Homeless']
    violence_crime_ratio = worksheet['Violence against the person ratio']
    sexual_crime_ratio = worksheet['Sexual offences ratio']
    robbery_crime_ratio = worksheet['Robbery ratio']
    theft_crime_ratio = worksheet['Theft offences ratio']
    damage_arson_crime_ratio = worksheet['Criminal damage and arson ratio']
    drug_crime_ratio = worksheet['Drug offences ratio']
    other_crime_ratio = worksheet['Other Crime Ratio']

    total_households_2020 = worksheet['total_households_projected_2020']
    households_with_children_ratio = worksheet['Year 2020: Households with dependent children ratio']
    one_female_households_ratio = worksheet['Year 2020: One person households: Female ratio']
    one_male_households_ratio = worksheet['Year 2020: One person households: Male ratio']
    pop_under_10_ratio = worksheet['pop_ratio_under_10']
    pop_teenager_ratio = worksheet['pop_ratio_teenager']
    pop_20_39_ratio = worksheet['pop_ratio_20_39']
    pop_40_60_ratio = worksheet['pop_ratio_40_60']
    pop_60_80_ratio = worksheet['pop_ratio_60_80']
    pop_80_90_ratio = worksheet['pop_ratio_80_90+']
    total_population_2020 = worksheet['POP All ages']
    size_of_la_area = worksheet['Total area as at 31 December 2020 (Hectares)']
    
    return worksheet,lower_quatile_earning_2020,ratio_by_lower_quatile_2020,median_earning_2020,ratio_by_medians_2020,month_rent_higher_quatile,month_rent_lower_quatile,total_threaten_homeless,violence_crime_ratio,sexual_crime_ratio,robbery_crime_ratio,theft_crime_ratio,damage_arson_crime_ratio,drug_crime_ratio,other_crime_ratio,total_households_2020,households_with_children_ratio,one_female_households_ratio,one_male_households_ratio,pop_under_10_ratio,pop_teenager_ratio,pop_20_39_ratio,pop_40_60_ratio,pop_60_80_ratio,pop_80_90_ratio,total_population_2020,size_of_la_area
    
def load_processed_quality_of_life_data():
    workbook = pd.ExcelFile('revised_all_in_one.xlsx')
    worksheet = workbook.parse(workbook.sheet_names[1])
    worksheet.index = list(range(0,len(list(worksheet['Numbering']))))
    worksheet = worksheet.drop(labels='Numbering',axis = 1)
    
    # Drivers and Taxi
    taxi_only_licensed_drivers = worksheet['Taxi_only_licensed_drivers']
    total_drivers = worksheet['total_drivers']
    
    # Size of Different Service Sectors
    retail_sector_size = worksheet['Retail']
    education_sector_size = worksheet['Education']
    health_sector_size = worksheet['Health']
    art_and_entertainment_sector_size = worksheet['Arts, entertainment, recreation & other services']
    
    return taxi_only_licensed_drivers,total_drivers,education_sector_size,health_sector_size,art_and_entertainment_sector_size
