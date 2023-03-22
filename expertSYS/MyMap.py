import os
import folium

# Avarage
# cfd = os.path.join(os.getcwd(), 'areas', 'CFD.geojson')
# vfd = os.path.join(os.getcwd(), 'areas', 'VFD.geojson')
allFab = os.path.join(os.getcwd(), 'areas', 'allFabric.geojson')
build1 = os.path.join(os.getcwd(), 'areas', 'building1.geojson')
build2 = os.path.join(os.getcwd(), 'areas', 'building2.geojson')
build3 = os.path.join(os.getcwd(), 'areas', 'building3.geojson')
# Norht
nwfo = os.path.join(os.getcwd(), 'areas', 'NWFO.geojson')
# South
sfo = os.path.join(os.getcwd(), 'areas', 'SFO.geojson')
ncfd = os.path.join(os.getcwd(), 'areas', 'NCFD.geojson')
# New
fefo = os.path.join(os.getcwd(), 'areas', 'FEFO.geojson')
urfo = os.path.join(os.getcwd(), 'areas', 'UrFO.geojson')
sfd = os.path.join(os.getcwd(), 'areas', 'SFD.geojson')


def get_html_all():
    mapObj = folium.Map(location=[55.856093, 49.039637], zoom_start=15)
    folium.GeoJson(allFab,
                   name='World').add_to(mapObj)
    # folium.GeoJson(fefo,
    #                name='World').add_to(mapObj)
    # folium.GeoJson(urfo,
    #                name='World').add_to(mapObj)
    # folium.GeoJson(sfd,
    #                name='World').add_to(mapObj)
    # folium.GeoJson(sfo,
    #                name='World').add_to(mapObj)
    # folium.GeoJson(vfd,
    #                name='World').add_to(mapObj)
    # folium.GeoJson(ncfd,
    #                name='World').add_to(mapObj)
    # folium.GeoJson(nwfo,
    #                name='World').add_to(mapObj)
    folium.LayerControl().add_to(mapObj)
    mapObj.save('main/templates/main/output.html')


def get_html_body():
    mapObj = folium.Map(location=[55.856093, 49.039637], zoom_start=15)
    folium.GeoJson(build1,
                   name='World').add_to(mapObj)
    # folium.GeoJson(ncfd,
    #                name='World').add_to(mapObj)
    folium.LayerControl().add_to(mapObj)
    mapObj.save('main/templates/main/output.html')


def get_html_glass():
    mapObj = folium.Map(location=[55.856093, 49.039637], zoom_start=15)
    folium.GeoJson(build2,
                   name='World').add_to(mapObj)
    folium.LayerControl().add_to(mapObj)
    mapObj.save('main/templates/main/output.html')


def get_html_fuel():
    mapObj = folium.Map(location=[55.856093, 49.039637], zoom_start=15)
    folium.GeoJson(build3,
                   name='World').add_to(mapObj)
    # folium.GeoJson(vfd,
    #                name='World').add_to(mapObj)
    folium.LayerControl().add_to(mapObj)
    mapObj.save('main/templates/main/output.html')


