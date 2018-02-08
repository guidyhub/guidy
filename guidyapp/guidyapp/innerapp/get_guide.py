from .models import Tour, Guide
from django.http import HttpResponse
from django.core import serializers

import logging

def main(request):
    guide = Guide.objects.filter(id=request.GET["id"])
    guide_json = serializers.serialize('json', guide)
    response = HttpResponse(guide_json, content_type='application/json')

    logging.info(response)

    return response
