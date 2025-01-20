# Crime-In-London
This repository contains the Python code I contributed to a university project, which focused on analysing crime data in London. The aim was to explore the relationships between various socio-economic factors and crime rates, as well as to create visualisations to support our findings. Using raw datasets, the project involved data preprocessing, feature impact analysis, and visualisation through heatmaps and GIFs.


Files:
- data_preparation.py - This script preprocesses and merges multiple datasets found on the internet to create a singular dataset for crime analysis. Key steps include:
  - Filtering and aggregating crime data by type and region (e.g., violent vs drug crimes).
  - Merging socio-economic datasets, including deprivation indices, employment rates, and public house density, with the crime data.
  - Calculating new features, such as total crimes by type and percentage employment rates.
  - Exporting the processed dataset for use in further analysis and modelling.
- feature_impact_analysis.py - This script evaluates the impact of modifying specific features (e.g., police officer deployment) on predicted crime rates in high-crime areas. The process includes:
  - Using a trained machine learning model to predict crime rates before and after modifying a feature.
  - Calculating percentage changes in predictions for the top crime areas (defined by a percentile threshold).
  - Visualising the results with bar charts that rank high-crime areas by percentage change in crime rates.
  - Saving the visual outputs for further analysis.
- crime_heatmap_generator.py - This script creates interactive crime heatmaps for London, using crime rates and geographic data. Features include:
  - Merging geographic boundary data with crime statistics.
  - Generating heatmaps with colour-coded crime rates, scaled logarithmically for better visualisation.
  - Saving the maps as interactive HTML files for easy sharing and exploration.
- create_gifs.py - This script generates animated GIFs to visualise changes in crime heatmaps over time or for comparison purposes. The process includes:
  - Identifying pairs of images (e.g., actual vs predicted crime heatmaps).
  - Compiling the images into looping GIFs with a user-defined animation speed.
  - Saving the GIFs in an output directory for use in presentations or reports.
 
Finally, there is a folder called 'Heatmaps', showing example heatmaps for three different crime types in a specific area of London. In the analysis of this report, we noted that the model does not accurately predict crime rates that well, shown by the difference between actual and predicted rates in the heatmap gifs. We concluded that our model likely didn't have enough features to train on and that we were held back by lack of usable data available on the internet, however our methodology could be reused with better data.
