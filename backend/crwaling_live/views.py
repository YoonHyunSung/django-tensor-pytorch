from django.http import JsonResponse
from icecream import ic
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from crwaling_live.scraper import covid_scraper
from crwaling_live.db_uploaders import DbUploader



@api_view(['GET'])
@parser_classes([JSONParser])
def crwaling(request):
    covid_scraper()
    return JsonResponse({'result':'sucess'})

@api_view(['GET'])
@parser_classes([JSONParser])
def uploader(request):
    DbUploader().insert_case()
    return JsonResponse({'result':'sucess'})







