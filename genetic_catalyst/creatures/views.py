from django.http import HttpRequest, JsonResponse


def index(_request: HttpRequest):
    return JsonResponse({"name": "creature"})
