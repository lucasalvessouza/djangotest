import json

import requests
from django.shortcuts import render
from .models import Quotes, Author


def index(request):
    quotes = Quotes.objects.all().values()
    if len(quotes) == 0:
        external_data = get_quotes()
        authors = [Author(**author) for author in external_data['authors']]
        Author.objects.bulk_create(authors)

        for quote in external_data['quotes']:
            author = Author.objects.get(id=quote['author_id'])
            quote['author_id'] = author
            Quotes.objects.bulk_create([Quotes(**quote)])

    authors = Author.objects.all().values()
    context = {
        'quotes': json.dumps(list(quotes)),
        'authors': json.dumps(list(authors))
    }
    return render(request, 'index.html', context)


def get_quotes():
    quotes_response = requests.get('https://www.scalablepath.com/api/test/test-quotes')
    authors_response = requests.get('https://www.scalablepath.com/api/test/test-authors')

    return {
        'quotes': quotes_response.json(),
        'authors': authors_response.json(),
    }
