from django.http import JsonResponse
from icecream import ic
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from crwaling_live.models import Crwaling_Live



@api_view(['GET'])
@parser_classes([JSONParser])
def (request):
    main()
    return JsonResponse({'result':'sucess'})

