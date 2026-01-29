import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")


st.sidebar.title("Agri_Performance")
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)



st.title("Thinking about Possibilities")
st.markdown(
    """
    This multipage app demonstrates the potential of today's technology
    """
)



st.header("Welcome")




m = leafmap.Map(center=[45.224461, -0.773946], zoom=16, minimap_control=True)
m.add_basemap("SATELLITE")
m.to_streamlit(height=500)