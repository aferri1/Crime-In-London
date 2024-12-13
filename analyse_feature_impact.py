#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 15:59:26 2024

@author: trekz1
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# def analyse_feature_impact(X_test, model, feature_names, feature_index, reduction_factor, percentile, crime_type):
#     """
#     Analyzes and visualizes the impact of reducing a specific feature by a given factor on crime predictions,
#     focusing on the highest crime areas defined by a percentile threshold and considering specific crime types.

#     Parameters:
#     - X_test (np.array): The test dataset.
#     - model (tf.keras.Model): Trained model for making predictions.
#     - feature_names (list): List of feature names corresponding to columns in X_test.
#     - feature_index (int): Index of the feature to modify.
#     - reduction_factor (float): Factor by which to reduce the feature (e.g., 0.2 for reducing by 20%).
#     - percentile (float): Percentile to define high-crime areas (e.g., 90 for top 10%).
#     - crime_type (str): Type of crime to focus the analysis on.

#     Returns:
#         mean_changes: Mean percentage change in crime predictions in high crime areas.
#     """
#     feature_name = feature_names[feature_index]
#     predictions_original = model.predict(X_test).flatten()
#     original_feature_values = X_test[:, feature_index].copy()

#     # Modifying the feature
#     X_modified = X_test.copy()
#     reduction_amount = original_feature_values * reduction_factor
#     X_modified[:, feature_index] = original_feature_values - reduction_amount
#     predictions_modified = model.predict(X_modified).flatten()

#     # Calculate the change in predictions
#     change_in_predictions = predictions_modified - predictions_original
#     percentage_change_in_predictions = (change_in_predictions / predictions_original) * 100  # Percentage change

#     # Determine the high-crime areas
#     threshold = np.percentile(predictions_original, percentile)
#     high_crime_indices = predictions_original >= threshold

#     # Focus on these high-crime areas
#     high_crime_percentage_changes = percentage_change_in_predictions[high_crime_indices]

#     # Sort these areas by the original prediction to highlight the biggest areas
#     sorted_indices = np.argsort(-predictions_original[high_crime_indices])
#     high_crime_percentage_changes_sorted = high_crime_percentage_changes[sorted_indices]

#     # Visualizing the change
#     plt.figure(figsize=(10, 6))
#     bars = plt.bar(range(len(high_crime_percentage_changes_sorted)), high_crime_percentage_changes_sorted, color='red')
#     plt.xlabel('Ranked High Crime Areas (Top {}%)'.format(100 - percentile))
#     plt.ylabel('Percentage Change in Predicted Crimes')
#     plt.title(f'Percentage Decrease in Predicted {crime_type} Crimes in Top {100 - percentile}% Areas')
#     plt.legend([bars], [f'{feature_name} reduced by {reduction_factor * 100}%'], loc='upper right')
#     plt.show()
    
#     mean_percentage_changes = np.mean(high_crime_percentage_changes)
#     print(f"Mean percentage change in {crime_type} crime predictions: {mean_percentage_changes}")
#     return mean_percentage_changes

# def analyse_feature_impact(X_test, model, feature_names, feature_name, reduction_factor, percentile, crime_type):
#     """
#     Analyzes and visualizes the impact of reducing a specific feature by a given factor on crime predictions,
#     focusing on the highest crime areas defined by a percentile threshold and considering specific crime types.

#     Parameters:
#     - X_test (np.array): The test dataset.
#     - model (tf.keras.Model): Trained model for making predictions.
#     - feature_names (Index or list): List or Index of feature names corresponding to columns in X_test.
#     - feature_name (str): Name of the feature to modify.
#     - reduction_factor (float): Factor by which to reduce the feature (e.g., 0.1 for reducing by 10%).
#     - percentile (float): Percentile to define high-crime areas (e.g., 90 for top 10%).
#     - crime_type (str): Type of crime to focus the analysis on.

#     Returns:
#         mean_changes: Mean percentage change in crime predictions in high crime areas.
#     """
#     reduction_factor = float(reduction_factor)  # Ensure reduction_factor is a float

#     if isinstance(feature_names, pd.Index):
#         feature_names = feature_names.tolist()
    
#     if feature_name not in feature_names:
#         raise ValueError(f"Feature name '{feature_name}' not found in feature names.")

#     feature_index = feature_names.index(feature_name)
#     predictions_original = model.predict(X_test).flatten()
#     original_feature_values = X_test[:, feature_index].copy()

#     X_modified = X_test.copy()
#     reduction_amount = original_feature_values * reduction_factor
#     X_modified[:, feature_index] = original_feature_values - reduction_amount
#     predictions_modified = model.predict(X_modified).flatten()

#     change_in_predictions = predictions_modified - predictions_original
#     percentage_change_in_predictions = (change_in_predictions / predictions_original) * 100

#     threshold = np.percentile(predictions_original, percentile)
#     high_crime_indices = predictions_original >= threshold

#     high_crime_percentage_changes = percentage_change_in_predictions[high_crime_indices]
#     sorted_indices = np.argsort(-predictions_original[high_crime_indices])
#     high_crime_percentage_changes_sorted = high_crime_percentage_changes[sorted_indices]

#     mean_percentage_changes = np.mean(high_crime_percentage_changes)

#     plt.figure(figsize=(10, 6))
#     bars = plt.bar(range(len(high_crime_percentage_changes_sorted)), high_crime_percentage_changes_sorted, color='red')
#     plt.xlabel('Ranked High Crime Areas (Top {}%)'.format(100 - percentile))
#     plt.ylabel('Percentage Change in Predicted Crimes')
#     # plt.title(f'Percentage Decrease in Predicted {crime_type} Crimes in Top {100 - percentile}% Areas')
#     plt.legend([bars], [
#         f'{feature_name} reduced by {reduction_factor * 100}%',
#         f'Mean Change: {mean_percentage_changes:.2f}%'
#     ], loc='upper right')
    
#     plt.annotate(f'Mean Change: {mean_percentage_changes:.2f}%', 
#              xy=(0.5, 0.9),  # Proper x, y coordinates within the axes
#              xycoords='axes fraction',  # Using axes fraction to place it relative to the axes size
#              textcoords='offset points',  # Offset in points from xy
#              xytext=(0, -10),  # Offset the text by -10 points vertically to place below the coordinate
#              ha='center',  # Center the text horizontally at the xy point
#              va='top')  # Vertically align the text at the top of the text box

        
#     filename = f"{crime_type.replace(' ', '_')}_{percentile}thPercentile_{feature_name.replace(' ', '_')}_{int(reduction_factor * 100)}.png"
#     plt.savefig(filename)
     
#     plt.show()

#     print(f"Mean percentage change in {crime_type} crime predictions: {mean_percentage_changes}")
#     return mean_percentage_changes

def analyse_feature_impact(X_test, model, feature_names, feature_name, change_factor, percentile, crime_type, increase=False):
    """
    Analyzes and visualizes the impact of modifying a specific feature by a given factor on crime predictions,
    focusing on the highest crime areas defined by a percentile threshold and considering specific crime types.

    Parameters:
    - X_test (np.array): The test dataset.
    - model (tf.keras.Model): Trained model for making predictions.
    - feature_names (Index or list): List or Index of feature names corresponding to columns in X_test.
    - feature_name (str): Name of the feature to modify.
    - change_factor (float): Factor by which to modify the feature (e.g., 0.2 for increasing or decreasing by 20%).
    - percentile (float): Percentile to define high-crime areas (e.g., 90 for top 10%).
    - crime_type (str): Type of crime to focus the analysis on.
    - increase (bool): Flag to indicate whether to increase (True) or decrease (False) the feature.

    Returns:
        mean_changes: Mean percentage change in crime predictions in high crime areas.
    """
    if isinstance(feature_names, pd.Index):
        feature_names = feature_names.tolist()
    
    if feature_name not in feature_names:
        raise ValueError(f"Feature name '{feature_name}' not found in feature names.")

    feature_index = feature_names.index(feature_name)
    predictions_original = model.predict(X_test).flatten()
    original_feature_values = X_test.iloc[:, feature_index].copy()

    # Modifying the feature
    X_modified = X_test.copy()
    if increase:
        # Increase the feature value by the specified change factor
        modification_amount = original_feature_values * (1 + change_factor)
    else:
        # Decrease the feature value by the specified change factor
        modification_amount = original_feature_values * (1 - change_factor)
    
    X_modified.iloc[:, feature_index] = modification_amount
    predictions_modified = model.predict(X_modified).flatten()

    # Calculate the change in predictions
    change_in_predictions = predictions_modified - predictions_original
    percentage_change_in_predictions = (change_in_predictions / predictions_original) * 100

    # Determine the high-crime areas
    threshold = np.percentile(predictions_original, percentile)
    high_crime_indices = predictions_original >= threshold

    # Focus on these high-crime areas
    high_crime_percentage_changes = percentage_change_in_predictions[high_crime_indices]

    mean_percentage_changes = np.mean(high_crime_percentage_changes)


    # Sort these areas by the original prediction to highlight the biggest areas
    sorted_indices = np.argsort(-predictions_original[high_crime_indices])
    high_crime_percentage_changes_sorted = high_crime_percentage_changes[sorted_indices]

    # Visualizing the change
    plt.figure(figsize=(10, 6))
    bars = plt.bar(range(len(high_crime_percentage_changes_sorted)), high_crime_percentage_changes_sorted, color='red' if not increase else 'green')
    plt.xlabel('Ranked High Crime Areas (Top {}%)'.format(100 - percentile))
    plt.ylabel('Percentage Change in Predicted Crimes')
    # plt.title(f'{"Increase" if increase else "Decrease"} in Predicted {crime_type} Crimes in Top {100 - percentile}% Areas due to {feature_name} Modification')
    plt.legend([bars], [f'{feature_name} {"increased" if increase else "reduced"} by {change_factor * 100}%'], loc='upper right')
    
    plt.annotate(f'Mean Change: {mean_percentage_changes:.2f}%', 
                  xy=(0.5, 0.9),  # Proper x, y coordinates within the axes
                  xycoords='axes fraction',  # Using axes fraction to place it relative to the axes size
                  textcoords='offset points',  # Offset in points from xy
                  xytext=(0, -10),  # Offset the text by -10 points vertically to place below the coordinate
                  ha='center',  # Center the text horizontally at the xy point
                  va='top')  # Vertically align the text at the top of the text box
            
    filename = f"{crime_type.replace(' ', '_')}_{percentile}thPercentile_{feature_name.replace(' ', '_')}_{int(change_factor * 100)}.png"
    plt.savefig(filename)
    
    plt.show()
    
    mean_percentage_changes = np.mean(high_crime_percentage_changes)
    abs_percentage_changes = abs(high_crime_percentage_changes)
    max_percentage_changes = max(abs_percentage_changes)
    print(f"Mean percentage change in {crime_type} crime predictions: {mean_percentage_changes}")
    print(max_percentage_changes)
    return mean_percentage_changes


# analyse_feature_impact(X_test,model,feature_names,'Officers_Assigned', 0.2, 99, 'Total', increase=True)













