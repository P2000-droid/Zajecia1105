# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 22:05:51 2021

@author: giera
"""
import geopandas as gpd 

import numpy as np
import matplotlib.pyplot as plt
import geopandas
gdf = geopandas.read_file("PD_STAT_GRID_CELL_2011.shp")
#gdf.to_crs("EPSG:4326") #układ
gdf['centroid'] = gdf.centroid #wyznaczenie centroid dla poligonóW

 

# wyznaczenie regularnej siatki
import shapely 
#
xmin, ymin, xmax, ymax = [13, 48, 25, 56]
#
n_cells = 30
cell_size = (xmax- xmin)/n_cells
#
grid_cells = []
for x0 in np.arange(xmin, xmax + cell_size, cell_size):
    for y0 in np.arange(ymin, ymax + cell_size, cell_size ):
        #bounds
        x1 = x0 - cell_size
        y1 = y0 + cell_size
        grid_cells.append(shapely.geometry.box(x0, y0, x1, y1))
cell = geopandas.GeoDataFrame(grid_cells, columns = ['geometry'])

 

ax = gdf.plot(markersize = .1, figsize = (12, 8), column = 'TOT', cmap = 'jet')

 

plt.autoscale(False)
cell.plot(ax = ax, facecolor = "none", edgecolor = 'grey')
ax.axis("off")

 

merged = geopandas.sjoin(gdf, cell, how = 'left', op = 'within')

 

dissolve = merged.dissolve(by = "index_right", aggfunc = "sum") #agregacja

 

cell.loc[dissolve.index, 'TOT'] = dissolve.TOT.values #przypisanie wartosci do oczek siatki

 

ax = cell.plot(column = 'TOT', figsize  =(12,8), cmap = 'viridis', vmax = 700000, edgecolor = "grey", legend = True)

 

plt.autoscale(False)        
ax.set_axis_off()
plt.axis('equeal')
plt.title('liczba ludnosci w siatce')