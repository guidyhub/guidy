from django.http import JsonResponse

def main(request):
    print(request)
    return JsonResponse({})