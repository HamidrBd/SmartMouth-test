import streamlit as st
from hydralit import HydraHeadApp
from streamlit_searchbox import st_searchbox
import folium

class Search(HydraHeadApp):
    """
    search the city.
    
    """

    def __init__(self, title = '', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title

    def run(self) -> None:
        col1, col2, col3 = st.columns(3)

        with col2:
            st.text_input(label="", placeholder="Enter cites or clinic name.")
        


        from streamlit_folium import st_folium

        # center on Liberty Bell, add marker
        m = folium.Map(location=[29.5926, 52.5836], zoom_start=16)
        folium.Marker(
            [29.5926, 52.5836], popup="Liberty Bell", tooltip="Liberty Bell"
        ).add_to(m)

        # call to render Folium map in Streamlit
        st_data = st_folium(m, width=2000, height=2000)

    
        
