import json,os, requests

def collect_taylor_swift_sources(API_KEY):
    """
    Collects all news sources from US discussing Taylor Swift 
    in the past month that have at least 1 article about them.
    """

    #open the file which is in the data folder
    path = os.path.join(os.getcwd(), "data")

    with open ('{}/sources_us.json'.format(path), 'r') as infile:
        data = json.load(infile)

    data = data['sources']
    sources = []

    for source in data:
        id = source['id']
        params = {
        'language': 'en',
        'sources': id,
        'sortBy': 'publishedAt',
        'apiKey': API_KEY,
        'q': 'Taylor Swift',
        }
        
        endpoint = 'https://newsapi.org/v2/everything'  
        response = requests.get(endpoint, params=params)
        response_json = response.json()

        if len(response_json['articles']) > 0:
            sources.append(id)

    path = os.path.join(os.getcwd(), "data")
    with open('{}/sources_us_articles_taylor_swift.json'.format(path), 'w') as outfile:
        json.dump(sources, outfile, indent=4)
        
    return sources