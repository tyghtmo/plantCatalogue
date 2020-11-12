import requests
import json
import os

# Trefle.io token as environmental variable
token = os.environ['TREFLETOKEN']


def get_all(page):
    # <page> url page object value
    # <return> Paginated JSON containing 30 plants

    url = 'https://trefle.io/api/v1/plants?token=' + token + '&page=' + page
    response = json.loads(requests.get(url).text)
    for link in response["links"]:
        response["links"][link] = '?' + str(response["links"][link]).split('?')[1]  # changes link from api to ?page=x
    return response


def get_single(slug):
    # <slug> unique plant identifier
    # <return> JSON for a single plant

    url = 'http://trefle.io/api/v1/plants/' + slug + "?token=" + token
    response = json.loads(requests.get(url).text)
    return response
