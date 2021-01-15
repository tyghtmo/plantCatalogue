import requests
import json
import os
import re

# Trefle.io token as environmental variable
token = os.environ['TREFLETOKEN']


def getPageLinks(links):
    # changes link in api to ?page=x

    for link in links:

        newLink = ''
        #finds and extracts ?page=999 from links 
        regex = r"[\?\&]{1}page{1}\=\d*"
        matches = re.findall(regex, links[link], re.MULTILINE)

        newLink = matches[0]

        links[link] = newLink.replace('&', '?')

    return links


def getPageAndSearchLinks(links):
    
    for link in links:

        newLink = ''
        #finds and extracts ?page=999 from links 
        regex = r"[\?\&]{1}page{1}\=\d*\&q=[a-zA-Z0-9]*"
        matches = re.findall(regex, links[link], re.MULTILINE)

        newLink = matches[0]

        links[link] = newLink
        
    return links


def get_all(page, parent):
    # <page> url page object value
    # <return> Paginated JSON containing 20 plants

    url = 'https://trefle.io/api/v1/' + parent + '?token=' + token + '&page=' + page 
    response = json.loads(requests.get(url).text)
    response['links'] = getPageLinks(response['links'])

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
    if 'links' in response:
        response['links'] = getPageAndSearchLinks(response['links'])

    return response

def get_children_from_parent(parent, child, page, slug):
    # <page> url page object value
    # <return> Paginated JSON containing 20 plants

    url = 'https://trefle.io/api/v1/' + parent + '/' + slug + '/' + child + '?token=' + token + '&page=' + page

    response = requests.get(url)

    if response.status_code == 200:
        response = json.loads(requests.get(url).text)
        response['links'] = getPageLinks(response['links'])

    return response
