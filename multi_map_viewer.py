import streamlit as st

def generate_map_url(map_service, latitude, longitude):
    if map_service == "HERE Maps":
        return f"https://maps.here.com/?map={latitude},{longitude},18"
    elif map_service == "Google Maps":
        # Embed URL for Google Maps
        return (
            f"https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!"
            f"1d25643.81035154141!2d{longitude}!3d{latitude}!"
            "2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!"
            "5e1!3m2!1sen!2suk!4v1732038984617!5m2!1sen!2suk"
        )
    elif map_service == "ArcGIS":
        return f"https://www.arcgis.com/apps/mapviewer/index.html?layers=10df2279f9684e4a9f6a7f08febac2a9&center={longitude},{latitude}&level=18"
    elif map_service == "Bing Maps":
        return f"https://www.bing.com/maps?cp={latitude}~{longitude}&lvl=18&style=h"
    elif map_service == "Mapbox":
        return f"https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v11.html?title=true&access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4M29iazA2Z2gycXA4N2pmbDZmangifQ.-g_vE53SD2WrJ6tFX7QHmA#18/{latitude}/{longitude}"
    elif map_service == "Satellites.pro":
        return f"https://satellites.pro/#{latitude},{longitude},18"
    else:
        return None

# Streamlit App
st.title("Multi-Map Coordinate Viewer")

st.markdown("Enter coordinates as comma-separated values (latitude, longitude).")

# Input Section
input_coordinates = st.text_input("Coordinates", "26.421306, 50.496418")

try:
    # Parse input into latitude and longitude
    latitude, longitude = map(float, input_coordinates.split(","))
    
    st.markdown("### Maps Display")
    st.markdown(f"Displaying maps for **Latitude**: {latitude} and **Longitude**: {longitude}")
    
    map_services = ["Satellites.pro", "Mapbox","Google Maps","ArcGIS", "HERE Maps", "Bing Maps",]
    
    for service in map_services:
        st.subheader(service)
        map_url = generate_map_url(service, latitude, longitude)
        if map_url:
            # Embed the iframe
            if service == "Google Maps":
                st.markdown(
                    f'<iframe src="{map_url}" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>',
                    unsafe_allow_html=True,
                )
            else:
                # Provide link and iframe for other services
                st.markdown(f"🔗 [Open {service}]({map_url})", unsafe_allow_html=True)
                st.markdown(
                    f'<iframe src="{map_url}" width="100%" height="500"></iframe>',
                    unsafe_allow_html=True,
                )
except ValueError:
    st.error("Please enter valid comma-separated values for coordinates (latitude, longitude).")
