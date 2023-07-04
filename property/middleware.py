from django.http import JsonResponse
from rest_framework import status

class ExceptionMiddleware(object):
    """
    Middleware that makes sure clients see a meaningful error message wrapped in a Json response.
    """    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if str(type(exception)) == "<class 'django.db.models.deletion.ProtectedError'>":
            data = {
                'error': {
                    'type':'Cannot delete this data - Protected',
                'message': 'Cannot delete the instance as it has a parent (foreign key) in some other model'}
            }
        else:
            data = {
            'error': {
                'type': str(type(exception)),
                'message': str(exception)
            }
        }
        return JsonResponse(data=data, status=status.HTTP_400_BAD_REQUEST)