import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd

st.set_page_config(layout="wide")


st.sidebar.title("Agri_Performance")
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)



st.title("Split-panel Map")



with st.expander("Explaination"):
    st.write('left panel shows the NDVI index')
    st.write('right panel shows ESA land cover as shown in the legend')

# gdf = gpd.read_file('/Users/deppa/PythonLuigi/GIS__GoogleEarthEngine__MattForrest_etc/QGis_software_practicing/Project_Lafite/Saved/A_NDVI.tiff')
# gdf2 = gpd.read_file("/Users/deppa/PythonLuigi/GIS__GoogleEarthEngine__MattForrest_etc/QGis_software_practicing/Project_Lafite/Saved/A.tiff")
m = leafmap.Map(center=[45.224461, -0.773946], zoom=14)
m.split_map(
    left_layer= m.add_gdf(gdf, layer_name="NDVI"),
    right_layer= m.add_gdf(gdf2, layer_name="Analysis")
)
m.add_legend(title="Peut_y_alet")

m.to_streamlit(height=700)