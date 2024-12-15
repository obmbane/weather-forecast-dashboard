import requests as rq

def get_api_data(location, number_of_days=None, option=None):
    
    api_key = '41228a6613ea78803ae4b65bddcf6b1a'
    city_name = location
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
    response = rq.get(url)

    data = response.json()

    return data

if __name__ == '__main__':
    content = get_api_data('Tokyo')
    print(content['list'][39])