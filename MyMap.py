import os
import folium
#Avarage
cfd = os.path.join(os.getcwd(),'areas','CFD.geojson')
vfd = os.path.join(os.getcwd(),'areas','VFD.geojson')
#Norht
nwfo = os.path.join(os.getcwd(),'areas','NWFO.geojson')
#South
sfo = os.path.join(os.getcwd(),'areas','SFO.geojson')
ncfd = os.path.join(os.getcwd(),'areas','NCFD.geojson')
#New
fefo = os.path.join(os.getcwd(),'areas','FEFO.geojson')
urfo = os.path.join(os.getcwd(),'areas','UrFO.geojson')
sfd = os.path.join(os.getcwd(),'areas','SFD.geojson')






def get_html_all():
    mapObj=folium.Map(location=[55.796392, 49.110657],zoom_start=5)
    folium.GeoJson(cfd,
                   name='World').add_to(mapObj)
    folium.GeoJson(fefo,
                   name='World').add_to(mapObj)
    folium.GeoJson(urfo,
                   name='World').add_to(mapObj)
    folium.GeoJson(sfd,
                   name='World').add_to(mapObj)
    folium.GeoJson(sfo,
                   name='World').add_to(mapObj)
    folium.GeoJson(vfd,
                   name='World').add_to(mapObj)
    folium.GeoJson(ncfd,
                   name='World').add_to(mapObj)
    folium.GeoJson(nwfo,
                   name='World').add_to(mapObj)
    folium.LayerControl().add_to(mapObj)
    mapObj.save('output/output.html')
def get_html_south():
    mapObj = folium.Map(location=[55.796392, 49.110657], zoom_start=5)
    folium.GeoJson(sfo,
                   name='World').add_to(mapObj)
    folium.GeoJson(ncfd,
                   name='World').add_to(mapObj)
    folium.LayerControl().add_to(mapObj)
    mapObj.save('output/output.html')
def get_html_north():
    mapObj = folium.Map(location=[55.796392, 49.110657], zoom_start=5)
    folium.GeoJson(nwfo,
                   name='World').add_to(mapObj)
    folium.LayerControl().add_to(mapObj)
    mapObj.save('output/output.html')
def get_html_avarage():
    mapObj = folium.Map(location=[55.796392, 49.110657], zoom_start=5)
    folium.GeoJson(cfd,
                   name='World').add_to(mapObj)
    folium.GeoJson(vfd,
                   name='World').add_to(mapObj)
    folium.LayerControl().add_to(mapObj)
    mapObj.save('output/output.html')
def get_html_new():
    mapObj = folium.Map(location=[55.796392, 49.110657], zoom_start=5)
    folium.GeoJson(fefo,name='World').add_to(mapObj)
    folium.GeoJson(urfo,name='World').add_to(mapObj)
    folium.GeoJson(sfd,name='World').add_to(mapObj)
    folium.LayerControl().add_to(mapObj)
    mapObj.save('output/output.html')
