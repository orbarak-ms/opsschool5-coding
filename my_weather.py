from requests import get
import sys

if len(sys.argv) < 3:
    print("Usage: python my_weather.py <city> <-c or -f>")
else:
    baseurl = "http://api.weatherstack.com/current?access_key=b3b4f38ef2e3ab941ec9981515769a3d&query="
    citieslist = sys.argv[1].split(",")
    units = sys.argv[2][1:2]
    if units == "c": units = "m"
    if units == "m":
        unitsname = "Celsius"
    else:
        unitsname = "Fahrenheit"

    for city in citieslist:
        res=get(''.join([baseurl,city,"&units=",units]))
        if 'current' not in res.json():
            print("City ", city, " doesn't exists. Partial list of the possible cities: Dublin, London, New York, Amsterdam",sep="")
        else:
            print("The weather in ", city, " today ", res.json()['current']['temperature']," ",unitsname,sep="")
