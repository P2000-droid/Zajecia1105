# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 22:05:51 2021

@author: giera
"""
import geopandas as gpd 

df = gpd.read_file(gpd.datasets.datasets.get_path('nybb'))

ax = df.plot(figsize = (10, 10), alpha=0.5, edgecolr = 'k' )


cities = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))
