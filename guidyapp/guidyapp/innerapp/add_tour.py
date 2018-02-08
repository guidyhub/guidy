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
            tour = Tour.objects.get(name=request.GET.get("tour_name", None))
            new_tt = TouristTour.objects.create(user = user, tour = tour, date = request.GET.get("date", None))
            new_tt.save()


    return JsonResponse({})

