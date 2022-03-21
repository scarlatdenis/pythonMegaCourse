import folium
map = folium.Map(location=[38.88, - 99.09],
                 zoom_start=6, tiles="Mapbox Bright")
map.save("Map1.html")

map.add_child(folium.Marker(location=[
              48.2, -99.1], popup="Hi, i am a Marker", icon=folium.Icon(color="green")))


# in terminal write: python3 map1.py
