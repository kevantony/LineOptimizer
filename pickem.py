import requests
import random





def process():
    url = "https://api.prizepicks.com/projections?league_id=124&per_page=250&single_stat=true"
    u = "https://api.prizepicks.com/projections?league_id=7&per_page=250&single_stat=true"
    headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Access-Control-Allow-Credentials': 'true',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://app.prizepicks.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9'
    }

    session = requests.Session()
    response = session.get(url, headers=headers)
    cookies = response.cookies
    #response = requests.get(u, headers=HEADERS)
    print(response)

    # Check the response status code
    if response.status_code == 200:
        # Request was successful
        data = response.json()
        # Process the data
        print(data)
    else:
        # Request failed
        print('Request failed with status code:', response.status_code)

if __name__ == '__main__':
    process()
