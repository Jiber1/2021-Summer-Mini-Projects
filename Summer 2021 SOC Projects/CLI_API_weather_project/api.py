import requests
import json
import pyfiglet
from plumbum import cli


with open("API_KEY.txt", "r") as API_file:
    API_KEY = API_file.read()


def get_weather(API_KEY, city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"

    response = requests.get(url).json()
    return response

def jsonfilesave(API_KEY, city_name):
    json_data = get_weather(API_KEY, city_name)
    if json_data['cod'] == '404':
        print("You have entered an invalid city")
        return
    with open("json_file.json","r+") as jf:
        jf.truncate(0)
        jf.close()
    kelvintemp = json_data['main']['temp']
    fahrenheittemp = (kelvintemp- 273.15) * (9/5) + 32
    with open('json_file.json', 'w', encoding='utf-8') as newfile:
        json.dump(json_data, newfile, ensure_ascii=False, indent=4)
        jf.close()
    print("it is " + str(fahrenheittemp) + " degrees out in " + city_name)

class WeatherCLI(cli.Application):
    VERSION = "1.0"
    weather = cli.Flag(['w', 'weather'], help="Gives the weather for a united states city") 

    def main(self):
        print(pyfiglet.figlet_format("Weather Tracker", font = "bubble"))

        while True:
            print("Enter a city in the US you want to look up or press q to quit")
            city = input()
            if (city == "q"):
                break
            else:
                city_name = city + ",US"
            jsonfilesave(API_KEY, city_name)

if __name__ == "__main__":
    WeatherCLI()

### TESTS

def test_get_files1():
    files = get_weather(API_KEY, "Chicago,us")
    assert len(files) > 0, "There should be json data for valid cities"

def test_get_files2():
    files = get_weather(API_KEY, "poop,us")
    assert len(files) == 2, "There should be a 404 error for invalid cities"

def test_jsonfilesave():
    files = jsonfilesave(API_KEY, "poop")
    assert files == None , "The result should be empty for an invalid city"


