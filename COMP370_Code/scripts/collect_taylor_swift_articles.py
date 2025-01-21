import os, json, requests

def collect_taylor_swift_articles(API_KEY):
    """
    Collects all news articles from US discussing Taylor Swift
    """
    taylor_us_sources_path = os.path.join(os.getcwd(), "data", "sources_us_articles_taylor_swift.json")
    with open (taylor_us_sources_path, 'r') as infile:
        data = json.load(infile)

    articles = []

    for source in data:

        # Set up the endpoint and parameters with Taylor Swift in the title
        endpoint = 'https://newsapi.org/v2/everything'
        params = {
            'language': 'en',
            'sources': source,
            'sortBy': 'publishedAt',
            'apiKey': API_KEY,
            'q': 'Taylor Swift',
            'searchIn': 'title'
        }

        # Make the request
        response = requests.get(endpoint, params=params)
        response_json = response.json()
        articles += response_json['articles']
    
    #output path
    path = os.path.join(os.getcwd(), "data")
    with open('{}/taylor_swift_articles.json'.format(path), 'w') as outfile:
        json.dump(articles, outfile, indent=4)