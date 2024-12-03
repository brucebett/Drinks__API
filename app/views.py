from django.shortcuts import render
from django.http import JsonResponse
from app.models import Drink
from .serializers import DrinkSerializer

# Create your views here.
def drink_list(request):
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return JsonResponse({"drinks": serializer.data}, safe=False)



