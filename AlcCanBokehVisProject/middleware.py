from django.http import JsonResponse
from django.conf import settings

class APIKeyValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        api_key = request.headers.get("X-Api-Key")
        if api_key != settings.API_KEY:
            return JsonResponse({'error': 'Invalid API key'}, status=403)
        
        response = self.get_response(request)
        return response
