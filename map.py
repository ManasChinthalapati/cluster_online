import streamlit as st
import geopandas as gpd
import pydeck as pdk

st.title("Display GPKG shapes in Streamlit (no Folium)")

# Load data
gdf = gpd.read_file("V1/clusters/AM_clusters.gpkg")

# Convert to WGS84 for web display
gdf = gdf.to_crs(4326)

# Convert GeoDataFrame to GeoJSON
geojson = gdf.__geo_interface__

# Compute map center
center = [gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()]

layer1 = pdk.Layer(
    "GeoJsonLayer",
    geojson,
    filled=True,               # Set to True if you want filled polygons
    stroked=True,
    #extruded=True,
    #get_elevation='properties.cluster_employees',
    #elevation_scale=0.5,
    get_fill_color=[204, 153, 0, 60],
    get_line_color=[204, 153, 0, 255],
    line_width_min_pixels=2
)




gdf = gpd.read_file("V1/clusters/CI_clusters.gpkg")

# Convert to WGS84 for web display
gdf = gdf.to_crs(4326)

# Convert GeoDataFrame to GeoJSON
geojson = gdf.__geo_interface__

# Compute map center
center = [gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()]

layer2 = pdk.Layer(
    "GeoJsonLayer",
    geojson,
    filled=True,               # Set to True if you want filled polygons
    stroked=True,
    #extruded=True,
    #get_elevation='properties.cluster_employees',
    #elevation_scale=0.5,
    get_fill_color=[128, 0, 128, 60],
    get_line_color=[128, 0, 128, 255],
    line_width_min_pixels=2
)



gdf = gpd.read_file("V1/clusters/DT_clusters.gpkg")

# Convert to WGS84 for web display
gdf = gdf.to_crs(4326)

# Convert GeoDataFrame to GeoJSON
geojson = gdf.__geo_interface__

# Compute map center
center = [gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()]

layer3 = pdk.Layer(
    "GeoJsonLayer",
    geojson,
    filled=True,               # Set to True if you want filled polygons
    stroked=True,
    #extruded=True,
    #get_elevation='properties.cluster_employees',
    #elevation_scale=0.5,
    get_fill_color=[0, 102, 204, 60],
    get_line_color=[0, 102, 204, 255],
    line_width_min_pixels=2
)


gdf = gpd.read_file("V1/clusters/FS_clusters.gpkg")

# Convert to WGS84 for web display
gdf = gdf.to_crs(4326)

# Convert GeoDataFrame to GeoJSON
geojson = gdf.__geo_interface__

# Compute map center
center = [gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()]

layer4 = pdk.Layer(
    "GeoJsonLayer",
    geojson,
    filled=True,               # Set to True if you want filled polygons
    stroked=True,
    #extruded=True,
    #get_elevation='properties.cluster_employees',
    #elevation_scale=0.5,
    get_fill_color=[200, 30, 30, 60],
    get_line_color=[200, 30, 30, 255],
    line_width_min_pixels=2
)


gdf = gpd.read_file("V1/clusters/LS_clusters.gpkg")

# Convert to WGS84 for web display
gdf = gdf.to_crs(4326)

# Convert GeoDataFrame to GeoJSON
geojson = gdf.__geo_interface__

# Compute map center
center = [gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()]

layer5 = pdk.Layer(
    "GeoJsonLayer",
    geojson,
    filled=True,               # Set to True if you want filled polygons
    stroked=True,
    #extruded=True,
    #get_elevation='properties.cluster_employees',
    #elevation_scale=0.5,
    get_fill_color=[255, 140, 0, 60],     # semi‑transparent
    get_line_color=[255, 140, 0, 255],
    line_width_min_pixels=2
)


gdf = gpd.read_file("V1/clusters/PBS_clusters.gpkg")

# Convert to WGS84 for web display
gdf = gdf.to_crs(4326)

# Convert GeoDataFrame to GeoJSON
geojson = gdf.__geo_interface__

# Compute map center
center = [gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()]

layer6 = pdk.Layer(
    "GeoJsonLayer",
    geojson,
    filled=True,               # Set to True if you want filled polygons
    stroked=True,
    #extruded=True,
    #get_elevation='properties.cluster_employees',
    #elevation_scale=0.5,
    get_fill_color=[160, 160, 160, 60],     # semi‑transparent
    get_line_color=[160, 160, 160, 255],
    line_width_min_pixels=2
)


view_state = pdk.ViewState(
    latitude=center[0],
    longitude=center[1],
    zoom=6,
    pitch=45,      # ✅ tilt camera to show 3D height
    bearing=0
)

# ✅ WORKS WITHOUT INTERNET – MapLibre basemap
deck = pdk.Deck(
    layers=[layer1, layer2, layer3, layer4, layer5, layer6],
    initial_view_state=view_state,
    map_provider="maplibre",
    map_style="https://basemaps.cartocdn.com/styles/positron/style.json"
)


st.pydeck_chart(deck)
#st.pydeck_chart(pdk.Deck(layers=[layer1, layer2, layer3, layer4], initial_view_state=view_state))
