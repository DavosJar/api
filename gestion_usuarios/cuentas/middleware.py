from django.http import JsonResponse
from .models import Aplicacion

class APIKeyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/api/'):
            api_key = request.headers.get('Authorization')

            if api_key:
                try:
                    aplicacion = Aplicacion.objects.get(api_key=api_key)
                    request.aplicacion = aplicacion
                except Aplicacion.DoesNotExist:
                    return JsonResponse({'error': 'Invalid API Key'}, status=401)

        response = self.get_response(request)
        return response