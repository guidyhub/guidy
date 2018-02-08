from django.conf import settings
from django.shortcuts import redirect
import requests
import json
from django.contrib.auth.models import User
from oauth2_provider.models import AccessToken
from datetime import datetime

glob_host = "http://localhost:8000"
client_id = "ETpNC9cGtXO78fFUZNSTW4rCfXRMWBPboaVg3rhC"
client_secret = "c8r8NnOcV6SYW769K1OrcMu1M1lZC7Ld4Tt5HIgt16pZWy1C8IqJdKRLsj3hR86Y8W4AmSmZJPdFN7DqxA4oCosIn9gfi1TYWz5OZPqk2bHirkW2U1Ev3hK08Dh8EvAu"

def main(request):
    response = None

    origin = request.META.get('HTTP_REFERER', 'http://localhost:3000')

    if request.GET.get("code", None) == None and response == None:
        return redirect(
            'https://www.facebook.com/v2.12/dialog/oauth?client_id=' +
            getattr(settings, "SOCIAL_AUTH_FACEBOOK_KEY", None) + '&redirect_uri=' +
            glob_host + '/facebook_login' +
            '&state=' + origin + '')

    else:
        origin = request.GET.get("state", None)
        response = requests.get(
            'https://graph.facebook.com/v2.12/oauth/access_token?client_id=' +
            getattr(settings, "SOCIAL_AUTH_FACEBOOK_KEY", None) + '&redirect_uri=' +
            glob_host + '/facebook_login&client_secret=' +
            getattr(settings, "SOCIAL_AUTH_FACEBOOK_SECRET", None) + '&code=' +
            request.GET.get("code", False))

        r = response.json()
        access_token = r['access_token']

        image = requests.get(
            'https://graph.facebook.com/me?fields=picture&access_token=' +
            access_token)
        image = image.json()
        url = image["picture"]["data"]["url"]

        payload = json.loads('{"grant_type": "convert_token", "client_id": "' + client_id +
                         '", "client_secret": "' + client_secret +
                         '", "backend": "facebook", "token": "' + access_token + '"}')

        response = requests.post("http://localhost:8000/auth/convert-token", data=payload)

        r = response.json()
        access_token = r['access_token']


        token_ = AccessToken.objects.get(token = access_token, expires__gt = datetime.now())
        user = User.objects.get(username = token_.user)

        user.avatar.url = url
        user.save()

        return redirect(origin + '?token=' + access_token)
