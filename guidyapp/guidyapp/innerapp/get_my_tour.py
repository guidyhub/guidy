from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from oauth2_provider.models import AccessToken
from datetime import datetime
from django.core import serializers
from guidyapp.innerapp.models import Tour, TouristTour

def main(request):
    token_ = request.META.get("HTTP_AUTHORIZATION", False)
    if token_:
        token_ = AccessToken.objects.get(token = token_.replace("bearer ", ""), expires__gt = datetime.now())
        if token_:
            user = User.objects.get(username=token_.user)
            tt = TouristTour.objects.filter(user__id=user.id)
            my_tours = Tour.objects.filter(id__in = tt)
            my_tours = serializers.serialize("json", my_tours)
            return HttpResponse(my_tours, content_type="application/json")
    return JsonResponse({})

