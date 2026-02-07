
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

import leafmap
import folium

#  GET DATA    These Files come all from QGIS
# gdf CRS is EPSG 4326.  It's a geographic not a Projection.  Unit is Degree
url = '/Users/deppa/PythonLuigi/GIS__GoogleEarthEngine__MattForrest_etc/QGis_software_practicing/Project_Lafite/parcelles_outlines.geojson'
gdf = gpd.read_file(url)
# gdf CRS is EPSG 4326.  It's a geographic not a Projection.  Unit is Degree
url_mildiou = '/Users/deppa/PythonLuigi/GIS__GoogleEarthEngine__MattForrest_etc/Notebook_Leafmap_Rasterio_etc_preStreamlit_develop/files/mildiou_shape_file/cep_mildiou_by_parcelleandvoronoi.shp'
gdf_mildiou = gpd.read_file(url_mildiou)
# gdf CRS is EPSG 4326.  It's a geographic not a Projection.  Unit is Degree
url_humidity = '/Users/deppa/PythonLuigi/GIS__GoogleEarthEngine__MattForrest_etc/Notebook_Leafmap_Rasterio_etc_preStreamlit_develop/files/point_humide_shape_file/points_humidity.shp'
gdf_Humidity_point = gpd.read_file(url_humidity)


# DATA SHAPING
gdf_Humidity_point.set_index('id', inplace=True)
gdf_mildiou = gdf_mildiou.drop(['id_2'], axis=1).rename(columns={'id':'id_plant', 'nom':'parcelle_name'})
gdf = gdf.rename(columns={'nom':'Parcelle_name'})
gdf = gdf.set_index('id')
# creo un altro GEODF con i soli centroid
#   METODO MIGLIORE
# la geometria la creo direttamente dagli Shaply points
from shapely import wkt
gdf2 = gdf1.filter(['centroid'])
gdf2['centroid'] = gdf2['centroid'].astype('str')
gdf2["Coordinates"] = gpd.GeoSeries.from_wkt(gdf2["centroid"])
gdf2 = gpd.GeoDataFrame(gdf2, geometry="Coordinates")


# DATA VISUALIZATION
m = leafmap.Map(center=[45.224461, -0.773946], zoom=17, height=700)
m.add_tile_layer(
    url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
    name="Google Satellite",
    attribution="Google",
)
point_style = {
    "radius": 5,
    "color": "blue",
    "fillOpacity": 0.8,
    "fillColor": "red",
    "weight": 3,
} 
point_style1 = {
    "radius": 5,
    "color": "red",
    "fillOpacity": 0.8,
    "fillColor": "blue",
    "weight": 3,
}   
point_style2 = {
    "radius": 5,
    "color": "yellow",
    "fillOpacity": 0.8,
    "fillColor": "yellow",
    "weight": 3,
}   

m.add_marker(location=[45.224461, -0.773946], draggable=True)
m.add_gdf(gdf)  
m.add_gdf(gdf2, point_style=point_style)
m.add_gdf(gdf_mildiou, point_style=point_style1)
m.add_gdf(gdf_Humidity_point, point_style=point_style2)

m


