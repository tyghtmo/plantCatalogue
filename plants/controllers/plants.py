import requests
import json
import os

# Trefle.io token as environmental variable
token = os.environ['TREFLETOKEN']


def cleanLinks(links):
    # changes link in api to ?page=x

    for link in links:
        links[link] = '?' + str(links[link]).split('?')[1]  
    return links


def get_all(page, parent):
    # <page> url page object value
    # <return> Paginated JSON containing 30 plants

    url = 'https://trefle.io/api/v1/' + parent + '?token=' + token + '&page=' + page
    response = json.loads(requests.get(url).text)
    response['links'] = cleanLinks(response['links'])

    return response


def get_single(slug, parent):
    # <slug> unique plant identifier
    # <return> JSON for a single plant

    url = 'http://trefle.io/api/v1/' + parent +'/' + slug + "?token=" + token
    response = json.loads(requests.get(url).text)
    return response

def search(query, page, parent):

    url = 'https://trefle.io/api/v1/' + parent +'/search?q=' + query + '&token=' + token + '&page=' + page
    response = json.loads(requests.get(url).text)
    response['links'] = cleanLinks(response['links'])

    return response
