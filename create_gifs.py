#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 13:25:29 2024

@author: trekz1
"""

import imageio
import os

def create_gifs(source_folder, output_folder):
    # Check if the output folder exists, if not, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Create a dictionary to hold pairs of images
    images_dict = {}

    # Loop through each file in the directory
    for filename in os.listdir(source_folder):
        # Identify the crime type from the filename
        if 'crimes.png' in filename and 'predicted' not in filename:
            crime_type = filename.replace(' crimes.png', '')
            predicted_file = f'predicted {crime_type} crimes.png'
            images_dict[crime_type] = [filename, predicted_file]

    # Generate GIFs for each pair
    for crime_type, files in images_dict.items():
        images = []
        for file in files:
            file_path = os.path.join(source_folder, file)
            if os.path.exists(file_path):
                images.append(imageio.imread(file_path))
            else:
                print(f"File not found: {file}")
                break
        else:
            # Create GIF only if both images were successfully loaded
            gif_path = os.path.join(output_folder, f"{crime_type} crimes.gif")
            try:
                # Save GIF with looping set to infinite and adjust duration to slow down the animation
                imageio.mimsave(gif_path, images, format='GIF', duration=2000, loop=0)
                print(f"GIF created for: {crime_type}")
            except Exception as e:
                print(f"An error occurred while creating the GIF: {e}")

                
        
# Specify the source and output folders
source_folder = '/Users/trekz1/Documents/MDM3/PhaseC/London_crime/heatmaps/heatmap images'  # Change this to your folder path with the images
output_folder = '/Users/trekz1/Documents/MDM3/PhaseC/London_crime/heatmaps/heatmap gifs'  # Specify where you want the GIFs saved

create_gifs(source_folder, output_folder)