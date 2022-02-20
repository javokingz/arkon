from django.shortcuts import render
from django.http import HttpResponse
from  .models import Position
from geopy.geocoders import Nominatim
from urllib import response
import requests
import ast

def save_data(request):
    """Vista para almacenar los datos de la API del cdmx.gob"""
    #args= {'vehicle_current_status': '1'}
    response = requests.get(url= "https://datos.cdmx.gob.mx/api/3/action/datastore_search?resource_id=ad360a0e-b42f-482c-af12-1fd72140032e")
    response.raise_for_status()

    geolocalizador= Nominatim(user_agent="myapp")
   
    data = response.json()


    positions = data["result"]["records"]
   
    for position in positions:
        position_id = position["id"]
        vei = position["vehicle_id"]
        geographic_point = position["geographic_point"]
        location = geolocalizador.reverse(position["geographic_point"])
        status =position["vehicle_current_status"]
        string = location.address
        alcaldia = string.split(",")
        position_data = Position(position_id, vei, geographic_point, alcaldia[3].strip(), status )

        position_data.save()
        
    html = "<html><body<h1>Done! </h1> </body></html>" 
    return HttpResponse(html)


def home(request):
    return render(request, "base.html")