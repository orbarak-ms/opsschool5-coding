from requests import get
import click

@click.command()
@click.option('--token', 'token', help='Token for my weather site')
@click.option('--city', 'city', help='List of cities')
@click.option('--T', 'Temper', help='Celsius or Fahrenheit')

def my_weather(token, city, Temper):

#    baseurl = "http://api.weatherstack.com/current?access_key=b3b4f38ef2e3ab941ec9981515769a3d&query="
    baseurl = "http://api.weatherstack.com/current?access_key={}&query=".format(token)
    citieslist = city.split(",")
    unitsname = Temper
    if unitsname == "Celsius":
        units = "m"
    else:
        units = "f"

    for city in citieslist:
        res=get(''.join([baseurl,city,"&units=",units]))
        if 'current' not in res.json():
            print("City ", city, " doesn't exists. Partial list of the possible cities: Dublin, London, New York, Amsterdam",sep="")
        else:
            print("The weather in ", city, " today ", res.json()['current']['temperature']," ",unitsname,sep="")

if __name__ == '__main__':
    my_weather()