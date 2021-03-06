from django.shortcuts import render
import json
from plants.controllers import plants

#region Lists
def plantList(requests):
    # <requests> Django state
    # <return> plantList.html rendered with the response JSON

    # Defaults to empty url page object
    page = ''
    if requests.GET.get('page'):
        page = requests.GET.get('page')

    response = plants.get_all(page, 'plants')
    return render(requests, 'lists/plantList.html', {
        'plants': response
    })


def genusList(requests):
    # <requests> Django state
    # <return> genusList.html rendered with the response JSON

    # Defaults to empty url page object
    page = ''
    if requests.GET.get('page'):
        page = requests.GET.get('page')

    response = plants.get_all(page, 'genus')
    return render(requests, 'lists/genusList.html', {
        'genus': response
    })


def familyList(requests):
    # <requests> Django state
    # <return> familyList.html rendered with the response JSON

    # Defaults to empty url page object
    page = ''
    if requests.GET.get('page'):
        page = requests.GET.get('page')

    response = plants.get_all(page, 'families')
    return render(requests, 'lists/familyList.html', {
        'family': response
    })


def orderList(requests):
    # <requests> Django state
    # <return> orderList.html rendered with the response JSON

    # Defaults to empty url page object
    page = ''
    if requests.GET.get('page'):
        page = requests.GET.get('page')

    response = plants.get_all(page, 'division_orders')
    return render(requests, 'lists/orderList.html', {
        'order': response
    })


def classList(requests):
    # <requests> Django state
    # <return> classList.html rendered with the response JSON

    # Defaults to empty url page object
    page = ''
    if requests.GET.get('page'):
        page = requests.GET.get('page')

    response = plants.get_all(page, 'division_classes')
    return render(requests, 'lists/classList.html', {
        'class': response
    })


#endregion

#region Singles
def plant(requests, slug):
    # <requests> Django state
    # <slug> unique plant identifier
    # <return> plant.html rendered with raw and pretty response JSON

    # Defaults to empty url page object
    page = ''
    if requests.GET.get('page'):
        page = requests.GET.get('page')

    response = plants.get_single(slug, 'plants')
    species = plants.get_children_from_parent('plants', 'species', page, slug)

    # JSON formatting for pretty printing
    pretty = json.dumps(response["data"], indent=4).replace('  ', '&emsp;')

    return render(requests, 'singles/plant.html', {
        'plant': response,
        'parsed': pretty,
        'species': species,
        'child_type': 'plants'
    })


def genus(requests, slug):
    # <requests> Django state
    # <slug> unique genus identifier
    # <return> genus.html rendered with response JSON

    page = getPage(requests)

    response = plants.get_single(slug, 'genus')
    children = plants.get_children_from_parent('genus', 'plants', page, slug)

    # JSON formatting for pretty printing
    pretty = json.dumps(response["data"], indent=4).replace('  ', '&emsp;')

    return render(requests, 'singles/single.html', {
        'parent': response,
        'parsed': pretty,
        'children': children,
        'child_type': 'plants'
    })


def family(requests, slug):
    # <requests> Django state
    # <slug> unique family identifier
    # <return> family.html rendered with response JSON

    page = getPage(requests)

    response = plants.get_single(slug, 'families')
    children = plants.get_children_from_parent('families', 'genus', page, slug)

    # JSON formatting for pretty printing
    pretty = json.dumps(response["data"], indent=4).replace('  ', '&emsp;')

    return render(requests, 'singles/single.html', {
        'parent': response,
        'parsed': pretty,
        'children': children,
        'child_type': 'genus'
    })


def order(requests, slug):
    # <requests> Django state
    # <slug> unique order identifier
    # <return> order.html rendered with response JSON

    page = getPage(requests)

    response = plants.get_single(slug, 'division_orders')
    children = plants.get_children_from_parent('division_orders', 'families', page, slug)

    # JSON formatting for pretty printing
    pretty = json.dumps(response["data"], indent=4).replace('  ', '&emsp;')

    return render(requests, 'singles/single.html', {
        'parent': response,
        'parsed': pretty,
        'children': children
    })


def divisionClass(requests, slug):
    # <requests> Django state
    # <slug> unique class identifier
    # <return> class.html rendered with response JSON

    page = getPage(requests)

    response = plants.get_single(slug, 'division_classes')
    children = plants.get_children_from_parent('divison_classes', 'division_orders', page, slug)

    # JSON formatting for pretty printing
    pretty = json.dumps(response["data"], indent=4).replace('  ', '&emsp;')

    return render(requests, 'singles/single.html', {
        'parent': response,
        'parsed': pretty,
        'children': children
    })
#endregion

#region Search
def query(requests):
    # <requests> Django state
    # <return> plantList.html rendered with the response JSON

    # Defaults to empty url page object
    page = '1'
    if requests.GET.get('page'):
        page = requests.GET.get('page')

    query = requests.GET.get('q')

    response = plants.search(query, page, 'plants')
    return render(requests, 'lists/plantList.html', {
        'plants': response
    })


#endregion

#region Helper Methods
def getPage(req):
    page = '1'
    if req.GET.get('page'):
        page = req.GET.get('page')

    return page


#endregion

