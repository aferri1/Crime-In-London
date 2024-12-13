#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:33:34 2024

@author: trekz1
"""
import pandas as pd

df = pd.read_csv('/Users/trekz1/Documents/MDM3/PhaseC/lsoa_data/MPS LSOA Level Crime (Historical) (1).csv')
big_df = pd.read_csv('/Users/trekz1/Documents/MDM3/PhaseC/London_crime/total_crimes_2021.csv')
dep_df = pd.read_csv('/Users/trekz1/Documents/MDM3/PhaseC/deprivation_index_2019.csv')
msoas = pd.read_csv('/Users/trekz1/Documents/MDM3/PhaseC/lsoa_data/PCD_OA_LSOA_MSOA_LAD_MAY22_UK_LU.csv', encoding='ISO-8859-1')
pubs = pd.read_csv('/Users/trekz1/Documents/MDM3/PhaseC/lsoa_data/features/publichousesandbarslondonmsoas20012020.csv')
employment = pd.read_csv('/Users/trekz1/Documents/MDM3/PhaseC/lsoa_data/features/economic activity per lsoa.csv')

major_categories = df['Major Category'].unique()
minor_categories = df['Minor Category'].unique()

# create df of 2021 data only
df_2021 = df.iloc[:,[0,3,4,145,144,143,142,141,140,139,138,137,136,135,134]]
# create dfs of violent crimes and drug crimes only
violent_df = df_2021[df_2021['Major Category'] == 'Violence Against the Person']
drug_df = df_2021[df_2021['Major Category'] == 'Drug Offences']

# sum total drug crimes in 2021 for each lsoa
drug_df['Total Drug Crimes'] = drug_df.iloc[:, 3:].sum(axis=1)
drug_df = drug_df.groupby('LSOA Code')['Total Drug Crimes'].sum().reset_index()

# sum total violent crimes in 2021 for each lsoa
violent_df['Total Violent Crimes'] = violent_df.iloc[:, 3:].sum(axis=1)
violent_df = violent_df.groupby('LSOA Code')['Total Violent Crimes'].sum().reset_index()



# # list of 2021 columns
# violent_columns_2021 = [col for col in violent_df.columns if str(col).startswith('2021')]
# # sum total violent crimes in 2021 
# violent_df['Total Violent Crimes'] = violent_df[violent_columns_2021].sum(axis=1)
# # filter df to contain only relevant columns
# violent_df = violent_df.iloc[:,[0,146]]

# # repeat for drug crimes
# drug_columns_2021 = [col for col in drug_df.columns if str(col).startswith('2021')]

# drug_df['Total Drug Crimes'] = drug_df[drug_columns_2021].sum(axis=1)

# drug_df = drug_df.iloc[:,[0,146]]


pubs = pubs.iloc[2:]

dep_df= dep_df.replace('\s+', '', regex=True)  # remove all spaces

dep_df = dep_df[dep_df['Measurement'] == 'Decile']  # filter out to only have decile rank

# pivot deprivation df:
pivoted_df = dep_df.pivot(index='FeatureCode',
                          columns='Indices of Deprivation',
                          values='Value').reset_index() 

# merge pivoted df into existing
big_df = big_df.merge(pivoted_df,
                      left_on='LSOA Code',
                      right_on='FeatureCode',
                      how='left')

# add corresponding msoas onto df
big_df = pd.merge(big_df,
                  msoas[['lsoa11cd','msoa11cd']].drop_duplicates('lsoa11cd'),
                  left_on='LSOA Code',
                  right_on='lsoa11cd',
                  how='left')

#add pub data onto big_Df
pubs_merge = pubs.columns[22]
pubs_index = pubs.columns[0]

big_df = big_df.merge(pubs[[pubs_index,pubs_merge]],
                      left_on='msoa11cd', 
                      right_on=pubs_index,
                      how='left')

# drop some irrelevant columns:
drop_columns = big_df.columns[[0,26,30,41,42,43]]
big_df.drop(drop_columns, axis=1, inplace=True)

# convert employment data to percentages
denom_index = 3  # index of column to be divided by
convert_indices = [4,5,6,7,8,9,10,11,12,13,14,15,16]  # columns that need converting

employment.iloc[:, convert_indices] = (employment.iloc[:, convert_indices].div(employment.iloc[:,denom_index],
                                         axis=0)) * 100

# merge employment :
employment.rename(columns={'LSOA code': 'LSOA Code'}, inplace=True)

big_df = big_df.merge(employment,
                      on='LSOA Code',
                      how='left')

drop_columns = big_df.columns[[39,40,41,55,56]]
big_df.drop(drop_columns, axis=1, inplace=True)

# rename last column
big_df = big_df.rename(columns={'Unnamed: 22':'Pubs per corresponding MSOA'})

# add total violent crimes & total drug crimes to the big df
big_df = pd.merge(big_df, violent_df[['LSOA Code', 'Total Violent Crimes']], on='LSOA Code', how='left')

big_df = pd.merge(big_df, drug_df[['LSOA Code', 'Total Drug Crimes']], on='LSOA Code', how='left')

# rearrange the columns
columns = list(big_df.columns)
new_columns_order = columns[:2] + columns[-2:] + columns[2:-2]
big_df = big_df[new_columns_order]

big_df.to_csv('/Users/trekz1/Documents/MDM3/PhaseC/London_crime/total_crimes_2021_updated.csv',index=False)




