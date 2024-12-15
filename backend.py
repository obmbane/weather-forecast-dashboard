import requests as rq

def get_api_data(location, number_of_days, option):
    
    api_key = '41228a6613ea78803ae4b65bddcf6b1a'
    city_name = location
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
    response = rq.get(url)

    data = response.json()
    print(data)
    complete_weather_data = data['list']                                #isolate relevant weather data
    requested_weather_data = complete_weather_data[:8*number_of_days]   #create a dataset based on the number of days requested by user
   # temp_list = []
   # date_list = []
    if option == 'Temperature':
        temp_list = [dict['main']['temp'] for dict in requested_weather_data]
        date_list = [dict['dt_txt'] for dict in requested_weather_data]

    return temp_list, date_list

if __name__ == '__main__':
    t, d = get_api_data(location='Tokyo',number_of_days=3,option='Temperature')
    #print(t)