#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 12:41:53 2024

@author: trekz1
"""

import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import folium
from folium import GeoJson, GeoJsonTooltip

lsoa_geo = gpd.read_file('/Users/trekz1/Documents/MDM3/PhaseC/lsoa_data/LSOA_Dec_2011_Boundaries_Generalised_Clipped_BGC_EW_V3_-5359576152338500277.geojson')
crime_data = pd.read_csv('/Users/trekz1/Documents/MDM3/PhaseC/lsoa_data/MPS LSOA Level Crime (Historical) (1).csv')
population_data = pd.read_csv('/Users/trekz1/Documents/MDM3/PhaseC/lsoa_data/features/sape23dt11mid2020lsoapopulationdensity.csv')
drug_data = pd.read_csv('drug_crimes_vs_predicted.csv')



#  crime data:

# cleaning crime dataset:
columns_2021 = [str(2021) + f'{month:02d}' for month in range(1, 13)]
crime_data['Total_2021'] = crime_data[columns_2021].sum(axis=1)  # sum months of 2021 to find total crimes in that year by 

# sum across crime types to find total crime per lsoa in 2021:
LSOA_2021 = crime_data.groupby('LSOA Code')['Total_2021'].sum().reset_index()

# min_rate, max_rate = 0.7, 4.7  # min and max of scale
# threshold_scale = np.linspace(min_rate, max_rate, 6).tolist()  # Creates 6 evenly spaced values

def generate_crime_heatmap(lsoa_geo, crime_data, crime_type, filename, threshold_scale):
    """
    Generates a heatmap of crime rates in London using LSOA boundary data and crime data.

    Parameters:
    - lsoa_geo: GeoDataFrame containing LSOA boundary data.
    - crime_data: DataFrame containing crime rates, must include columns 'LSOA Code' and '{crime_type}_2021'.
    - crime_type: String specifying the type of crime (e.g., 'Violent').
    - threshold_scale: scale that you want crime to be. If you want it done 
        automatically then delete this parameter and comment the command below
    - filename: String specifying the filename where the heatmap will be saved.
    """
    # Ensure the column exists for the specified crime type
    crime_column = f'{crime_type}_2021'
    if crime_column not in crime_data.columns:
        raise ValueError(f"Crime data does not contain column: {crime_column}")

    # Merge the GeoDataFrame with the crime data
    merged_data = lsoa_geo.merge(crime_data, left_on='LSOA11CD', right_on='LSOA Code')
    merged_data['Log_Crime_Rate'] = np.log1p(merged_data[crime_column])

    # Create a base map over central London
    m = folium.Map(location=[51.5074, -0.1278], zoom_start=12)

    # Add the heatmap (choropleth)
    folium.Choropleth(
        geo_data=merged_data,
        name='choropleth',
        data=merged_data,
        columns=['LSOA Code', 'Log_Crime_Rate'],
        key_on='feature.properties.LSOA Code',
        fill_color='OrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        threshold_scale = threshold_scale,  # comment this if you want it done automatically
        legend_name=f'{crime_type} Crimes (Log Scaled)'
    ).add_to(m)

    folium.LayerControl().add_to(m)

    m.save(filename)
    print(f"Map saved to {filename}")

























































