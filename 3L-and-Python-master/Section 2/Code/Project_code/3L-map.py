import pandas as pd
import geopandas as gp
import matplotlib.pyplot as plt
import os
from shapely.geometry import Point


## Setting project root directory
os.chdir("/Users/demilson.fayika/Documents/Data")

## uk_airport_coords dataframe
uk_airport_coords = pd.read_csv("uk_airport_coords.csv")

## See the first 5 entries of the uk_airport dataframe
print(uk_airport_coords.head())

## Print the uk_airport object type
print(type(uk_airport_coords))

## Define geometry (fill in Longitude and Latitude in the right order)
geometry = [Point(xy) for xy in zip(uk_airport_coords['Longitude'], uk_airport_coords['Latitude'])]

# Assign coordinate reference system : WGS84
crs = {'init': 'epsg:4326'}

# Creating a geographic data frame
uk_airport_coords_gdf = gp.GeoDataFrame(uk_airport_coords, crs=crs, geometry=geometry)
print(uk_airport_coords_gdf.head())
uk_airport_coords_gdf.plot(marker='o', color='#3e3e3e', markersize=10)

# view the plot in a new window
plt.show()