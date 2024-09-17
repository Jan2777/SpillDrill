import streamlit as st
import folium
from streamlit_folium import st_folium

st.title('Simple Map Test')

# Create a basic map
m = folium.Map(location=[51.5074, -0.1278], zoom_start=10)  # Centered on London

# Render map in Streamlit
st_folium(m, width=700, height=500)
