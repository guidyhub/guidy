from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import redirect
import requests
import json
import unicodedata

glob_host = "http://localhost:8000"
client_id = "dskNJyfJqbZTg1KPZEwpkrugaZCxxMLEohjCcUfL"
client_secret = "q48PWcwBaJGEmSilQJ9RrqMrrWSM1dhEhvVPZckMlh0B9LIT7MIOJjipJjiFrRQvX6DZKnAhAvWDliDxi6BQbY35deXmqiyJLwxQDj7iL30mWlmZWk7GQhNPWKhM81K8"
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def main(request):
    response = None
    origin = request.META['HTTP_REFERER']
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

        payload = json.loads('{"grant_type": "convert_token", "client_id": "' + client_id +
                         '", "client_secret": "' + client_secret +
                         '", "backend": "facebook", "token": "' + access_token + '"}')

        response = requests.post("http://localhost:8000/auth/convert-token", data=payload)

        r = response.json()
        access_token = r['access_token']

        print(access_token)

        return redirect(origin + '?token=' + access_token)
        #response = requests.get('https://graph.facebook.com/v2.12/oauth/access_token?client_id=147786719252696&redirect_uri=http://localhost:3000&client_secret=b16c700d3aae95f4433914e530322bb5&code='+code)
