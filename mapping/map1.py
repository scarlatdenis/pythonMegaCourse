
from textwrap import fill
from turtle import color, fillcolor
import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation >= 3000:
        return "orange"
    else:
        return "red"


map = folium.Map(location=[38.1997986, -99.1809998],
                 zoom_start=4, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], radius=6, popup=str(el) + " m",
                               fill_color=color_producer(el), color="grey", fill_opacity=0.7))

fg.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig"),
                            style_function=lambda x: {'fillColor': 'yellow'}))


map.add_child(fg) 

map.save("Map1.html")


# in terminal write: python3 map1.py
