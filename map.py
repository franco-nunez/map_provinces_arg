# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 19:53:26 2023

@author: Franco
"""

#pip install geopandas matplotlib
#pip install cartopy

import os
import geopandas as gpd
import matplotlib.pyplot as plt 
import cartopy.crs as ccrs
from cartopy.io.shapereader import Reader as sf
from cartopy.feature import ShapelyFeature as cfeature

directory = "G:\\My Drive\\SHARES\\1_Paises\\Argentina\\Modelos\\Politics\\Provinces map"
#directory = 'G:\\Mi unidad\\SHARES\\1_Paises\\Argentina\\Modelos\\Precios online\\Dia'

os.chdir(directory)


# Load Argentina's provinces shapefile
shapefile_path = "provincia.shp"
gdf = gpd.read_file(shapefile_path)


############################################
# 2nd approach 
# https://es.stackoverflow.com/questions/367887/graficar-mapa-argentina-con-archivo-shp-python
fname = 'provincia.shp'

fig, ax = plt.subplots( 1, 1, subplot_kw=dict(projection=ccrs.PlateCarree()), figsize=[12,14]  )
shape_feature = cfeature(sf(fname).geometries(), ccrs.PlateCarree(), edgecolor='black')
ax.add_feature(shape_feature, facecolor= 'none')

#Defino los ejes (lon min y max, lat min y max)
ax.set_extent([-76, -53, -57, -20])


