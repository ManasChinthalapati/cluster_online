import streamlit as st
import geopandas as gpd
import pydeck as pdk
from pathlib import Path

st.title("Display GPKG shapes in Streamlit")

# ----------------------------
# Sidebar controls
# ----------------------------
st.sidebar.header("Layers")

layer_config = {
    "Advanced Manufacturing": {
        "file": "AM_clusters.gpkg",
        "color": [204, 153, 0, 60],
        "line": [204, 153, 0, 255],
        "key": "AM"
    },
    "Creative Industries": {
        "file": "CI_clusters.gpkg",
        "color": [128, 0, 128, 60],
        "line": [128, 0, 128, 255],
        "key": "CI"
    },
    "Digital & Tech": {
        "file": "DT_clusters.gpkg",
        "color": [0, 102, 204, 60],
        "line": [0, 102, 204, 255],
        "key": "DT"
    },
    "Financial Services": {
        "file": "FS_clusters.gpkg",
        "color": [200, 30, 30, 60],
        "line": [200, 30, 30, 255],
        "key": "FS"
    },
    "Life Sciences": {
        "file": "LS_clusters.gpkg",
        "color": [255, 140, 0, 60],
        "line": [255, 140, 0, 255],
        "key": "LS"
    },
    "Professional & Business Services": {
        "file": "PBS_clusters.gpkg",
        "color": [160, 160, 160, 60],
        "line": [160, 160, 160, 255],
        "key": "PBS"
    }
}

selected_layers = []
layers = []
centers = []

# ----------------------------
# Load layers based on checkboxes
# ----------------------------
for name, cfg in layer_config.items():
    if st.sidebar.checkbox(name, value=True, key=cfg["key"]):
        gdf = gpd.read_file(Path(cfg["file"])).to_crs(4326)
        geojson = gdf.__geo_interface__

        centers.append([
            gdf.geometry.centroid.y.mean(),
            gdf.geometry.centroid.x.mean()
        ])

        layers.append(
            pdk.Layer(
                "GeoJsonLayer",
                geojson,
                filled=True,
                stroked=True,
                pickable=True,
                get_fill_color=cfg["color"],
                get_line_color=cfg["line"],
                line_width_min_pixels=2
            )
        )

# ----------------------------
# Map view
# ----------------------------
if centers:
    avg_lat = sum(c[0] for c in centers) / len(centers)
    avg_lon = sum(c[1] for c in centers) / len(centers)
else:
    avg_lat, avg_lon = 54.5, -2.5  # fallback (UK centre)

tooltip = {
    "html": """
    <b>Turnover:</b> {cluster_turnover}<br/>
    <b>Employees:</b> {cluster_employees}
    """,
    "style": {
        "backgroundColor": "white",
        "color": "black"
    }
}

view_state = pdk.ViewState(
    latitude=avg_lat,
    longitude=avg_lon,
    zoom=6,
    pitch=45,
)

deck = pdk.Deck(
    layers=layers,
    initial_view_state=view_state,
    map_provider="maplibre",
    map_style="https://basemaps.cartocdn.com/styles/positron/style.json",
    tooltip=tooltip
)

st.pydeck_chart(deck, use_container_width=True, height=700)
