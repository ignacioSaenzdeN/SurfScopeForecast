from fantasyleague.models import FantasyLeague
from ..models import *
from .serializers import *
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
# from django.core.serializers import serialize


@api_view(['GET', 'PUT', 'DELETE'])
def surfersView(request):
    try:
        surfers = FantasyLeague.objects.values()
    except surfers.DoesNotExist:
        return JsonResponse({'message': 'The user surfing info does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        surfers_serializer = FantasyLeagueSerializer(surfers,  many=True)
        print(surfers_serializer.data)
        return JsonResponse(surfers_serializer.data,  safe=False)
