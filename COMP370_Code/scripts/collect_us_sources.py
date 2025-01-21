import json, os, requests

def collect_us_sources(API_KEY):
    """
    Collects all American sources from the NewsAPI and saves
    them to JSON files.
    """

    params = {
        "country": "us",
        "language": "en",
        "apiKey": API_KEY,
    }

    endpoint = "https://newsapi.org/v2/sources"

    data = requests.get(endpoint, params=params)

    #save inside the data folder
    path = os.path.join(os.getcwd(), "data")
    with open('{}/sources_us.json'.format(path), 'w') as outfile:
        json.dump(data.json(), outfile, indent=4)