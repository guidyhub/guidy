from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from oauth2_provider.models import AccessToken
from datetime import datetime
from django.core import serializers

def main(request):
    token_ = request.META.get("HTTP_AUTHORIZATION", False)
    if token_:
        token_ = AccessToken.objects.get(token = token_.replace("bearer ", ""), expires__gt = datetime.now())
        if token_:
            user = User.objects.filter(username = token_.user).defer("password")
            user = serializers.serialize("json", user)
            return HttpResponse(user, content_type="application/json")
    return JsonResponse({})