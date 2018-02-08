from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from oauth2_provider.models import AccessToken
from guidyapp.innerapp.models import Avatar

from datetime import datetime
from django.core import serializers
import json

def main(request):
    token_ = request.META.get("HTTP_AUTHORIZATION", False)
    if token_:
        token_ = AccessToken.objects.get(token = token_.replace("bearer ", ""), expires__gt = datetime.now())
        if token_:
            user = User.objects.get(username = token_.user)
            ava = Avatar.objects.get(user=user)
            user = json.dumps({'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email, 'avatar': ava.url})
            return HttpResponse(user, content_type="application/json")
    return JsonResponse({})