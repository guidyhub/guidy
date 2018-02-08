from .models import Tour
from django.http import HttpResponse
from django.core import serializers

import logging


def main(request):
    all_tours = Tour.objects.all()

    all_tours_json = serializers.serialize('json', all_tours)
    response = HttpResponse(all_tours_json, content_type='application/json')

    logging.info(response)

    return response
