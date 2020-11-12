from django.shortcuts import render
import json
from plants.controllers import plants


def index(requests):
    # <requests> Django state
    # <return> index.html rendered with the response JSON

    # Defaults to empty url page object
    page = ''
    if requests.GET.get('page'):
        page = requests.GET.get('page')

    response = plants.get_all(page)
    return render(requests, 'index.html', {
        'plants': response
    })


def plant(requests, slug):
    # <requests> Django state
    # <slug> unique plant identifier
    # <return> plant.html rendered with raw and pretty response JSON

    response = plants.get_single(slug)

    # JSON formatting for pretty printing
    pretty = json.dumps(response["data"], indent=4).replace('  ', '&emsp;')

    return render(requests, 'plant.html', {
        'plant': response,
        'parsed': pretty,
    })
