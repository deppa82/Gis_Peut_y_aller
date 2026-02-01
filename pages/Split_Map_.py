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

url1 = 'https://github.com/deppa82/Gis_Peut_y_aller/blob/main/Saved/C.svg'
url2 = 'https://github.com/deppa82/Gis_Peut_y_aller/blob/main/Saved/C.svg'
m = leafmap.Map(center=[45.224461, -0.773946], zoom=17)
m.split_map(left_layer=url1,right_layer=url2)
m.add_legend(title="Peut_y_alet")

m.to_streamlit(height=700)
