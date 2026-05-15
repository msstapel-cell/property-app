import streamlit as st
import pandas as pd
import pydeck as pdk

# Pagina instellingen
st.set_page_config(layout="wide", page_title="Ravi Sharma Dashboard")

st.title("🇦🇺 Ravi Sharma's Property Hotspot Finder")

# TEST DATA (Later koppelen we dit aan je eigen Excel/Google Sheet)
data = pd.DataFrame({
    'suburb': ['Armadale (WA)', 'Elizabeth (SA)', 'Rockingham (WA)', 'Logan Central (QLD)', 'Bundaberg (QLD)'],
    'lat': [-32.14, -34.71, -32.27, -27.63, -24.86],
    'lon': [116.01, 138.66, 115.72, 153.10, 152.34],
    'yield': [6.2, 7.5, 5.8, 6.4, 6.9],
    'vacancy': [0.4, 0.3, 0.5, 0.8, 0.6]
})

# Sidebar filters
st.sidebar.header("Filters")
min_yield = st.sidebar.slider("Minimale Yield (%)", 0.0, 10.0, 5.5)
max_vacancy = st.sidebar.slider("Maximale Vacancy (%)", 0.0, 3.0, 1.0)

# Filteren van de data
filtered_df = data[(data['yield'] >= min_yield) & (data['vacancy'] <= max_vacancy)]

# Kaart tonen
st.subheader(f"Gevonden locaties: {len(filtered_df)}")
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(latitude=-25.27, longitude=133.77, zoom=3),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            filtered_df,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=50000,
        ),
    ],
))

# Tabel tonen
st.write(filtered_df)
