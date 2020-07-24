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
    

map = folium.Map(location= [38.58, -99.09],tiles="Stamen Toner", zoom_start= 4)
feature = folium.FeatureGroup(name="My Pop Map")

for lt, ln, el, nm in zip(vol_lat, vol_long, vol_elev, vol_name):
    iframe = folium.IFrame(html = html % (nm, nm, el), width= 150, height= 75)
    feature.add_child(folium.Marker(location= [lt, ln], popup= folium.Popup(iframe), icon= folium.Icon(color=colour(el))))

map.add_child(feature)
map.save("pop-map.html")



