import http.client
import urllib.parse
import json, os

def collect_taylor_swift_mediastack(ACCESS_KEY):
    conn = http.client.HTTPConnection('api.mediastack.com')

    params = urllib.parse.urlencode({
        'access_key': ACCESS_KEY,
        'languages': 'en',
        'countries': 'us',
        'keywords': 'Taylor Swift',
        'limit': 100,
    })

    conn.request('GET', '/v1/news?{}'.format(params))

    res = conn.getresponse()
    data = res.read()

    # Decode the byte data to string
    decoded_data = data.decode('utf-8')

    # Parse the string data into a Python object (assuming it's JSON)
    json_data = json.loads(decoded_data)

    # Close the connection
    conn.close()

    path = os.path.join(os.getcwd(), "data")
    # Dump the data into a JSON file
    with open('{}/mediastack_output.json'.format(path), 'w') as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

    # Extract and filter relevant information
    articlecount = 0
    filtered_data = []
    for article in json_data['data']:
        title = article['title']
        if 'Taylor Swift' in title:
            url = article['url']
            description = article['description']
            filtered_data.append({'title': title, 'url': url, 'description': description})
            articlecount +=1
    print(articlecount)

    # Dump the filtered data into a separate JSON file
    with open('{}/mediastack_filtered_output.json'.format(path), 'w') as filtered_json_file:
        json.dump(filtered_data, filtered_json_file, indent=4, ensure_ascii=False)
