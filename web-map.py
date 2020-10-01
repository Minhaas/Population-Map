import folium
import pandas 

vol_data = pandas.read_csv("Volcanoes.txt")
vol_lat = list(vol_data["LAT"])
vol_long = list(vol_data["LON"])
vol_elev = list(vol_data["ELEV"])
vol_name = list(vol_data["NAME"])

html = """ VOLCANO NAME: <br> 
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
HEIGHT: %s m """

def colour(elev):
    if elev < 1000:
        return 'green'
    elif 1000 <= elev < 3000:
        return 'orange'
    else: 
        return 'black'
    

map = folium.Map(location= [20.5937, 78.9629],tiles="Stamen Toner", zoom_start= 5)
feature = folium.FeatureGroup(name="Population map layer")

for lt, ln, el, nm in zip(vol_lat, vol_long, vol_elev, vol_name):
    iframe = folium.IFrame(html = html % (nm, nm, el), width= 150, height= 75)
    feature.add_child(folium.CircleMarker(location= [lt, ln], radius=7, popup= folium.Popup(iframe), fill_color = colour(el), color = 'grey', fill_opacity = 0.7))

feature.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 30000000 else 'red'}))

map.add_child(feature)
map.add_child(folium.LayerControl(position= 'topright', collapsed= True))

map.save("index.html")



