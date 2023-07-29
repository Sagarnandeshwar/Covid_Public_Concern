import requests
import os
import json

os.environ['TOKEN'] = ''


def auth():
    return os.getenv('TOKEN')

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def create_url(keyword, max_results = 10):
    
    search_url = "https://api.twitter.com/2/tweets/search/all" 

    query_params = {'query': keyword,
                    'max_results': max_results,
                    'next_token': {}}

    query_params = {'query': keyword}
    return (search_url, query_params)

def connect_to_endpoint(url, headers, params, next_token = None):
    params['next_token'] = next_token
    response = requests.request("GET", url, headers = headers, params = params)
    
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    
    return response.json()


def main():
    
    bearer_token = auth()
    headers = create_headers(bearer_token)
    keyword = "covid lang:en"
    max_results = 10
    
    url = create_url(keyword, max_results)

    #print(url)

    json_response = connect_to_endpoint(url[0], headers, url[1])
    
    print(json.dumps(json_response, sort_keys=True))


if __name__ == "__main__":
    main()
