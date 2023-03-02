from django.http import HttpRequest
from rest_framework.throttling import UserRateThrottle


def setup_useragent_on_request_middleware(get_response):
    print("Install call")

    def middleware(request: HttpRequest):
        print("Before get response")
        response = get_response(request)
        print("After get response")
        return response
    return middleware


class CountRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.responses_count = 0
        self.exceptions_count = 0

    def __call__(self, request: HttpRequest):
        self.requests_count += 1
        print("Requests count", self.requests_count)
        response = self.get_response(request)
        self.responses_count += 1
        print("Responses count", self.responses_count)
        return response

    def process_exception(self, request: HttpRequest, exception: Exception):
        self.exceptions_count += 1
        print("Got", self.exceptions_count, "exception so far")


# TODO задание состоит в написании собственной middleware, а не в использовании готовой. Если есть сложности с этим,
#  даю подсказку алгоритма:
#  - храним данные по посещениях в словаре
#  - при запросе смотрим в словарь по ключу с ip, если его нет, создаём запись вида "ip: время доступа", и всё,
#  а если ключ есть, то получаем время прошлого доступа
#  - сравниваем текущее время и время последнего запроса, если разница меньше допустимого - возвращаем страницу
#  с ошибкой. Если разница допустима - обновляем время доступа для этого ip.
class BurstRateThrottle(UserRateThrottle):
    scope = 'burst'


class SustainedRateThrottle(UserRateThrottle):
    scope = 'sustained'


REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'example.throttles.BurstRateThrottle',
         'example.throttles.SustainedRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'burst': '60/min',
        'sustained': '1000/day'
    }
}

