import folium

map = folium.Map(location=[47.022496, 28.770363],
                 zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

fg.add_child(folium.Marker(location=[
    47.022, 28.77], popup="Here is Larisa", icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("Map1.html")


# in terminal write: python3 map1.py
