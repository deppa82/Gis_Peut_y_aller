import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")


st.sidebar.title("Agri_Performance")
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)


st.title("Interactive Map")



col1, col2 = st.columns([4, 1])
options = list(leafmap.basemaps.keys())
index = options.index("OpenTopoMap")

with col2:

    basemap = st.selectbox("Select a basemap:", options, index)

with col1:

    m = leafmap.Map(
        center=[45.224461, -0.773946], zoom=10,locate_control=True, latlon_control=True, 
        draw_export=True, minimap_control=True
        
    )
    m.add_basemap(basemap)
    m.to_streamlit(height=700)