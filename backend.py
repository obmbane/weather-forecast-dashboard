import requests as rq

def get_api_data(location, number_of_days):
    
    api_key = '41228a6613ea78803ae4b65bddcf6b1a'
    city_name = location
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
    response = rq.get(url)

    data = response.json()
    complete_weather_data = data['list']                                #isolate relevant weather data
    working_dataset = complete_weather_data[:8*number_of_days]   #create a dataset based on the number of days requested by user

    return working_dataset

if __name__ == '__main__':
    display_data = get_api_data(location='Tokyo',number_of_days=3)
    print(display_data)