from django.http import HttpResponse
from rest_framework import generics
from .models import Scrap
from .serializers import ScrapSerializer

def index(request):
    return HttpResponse("Hello, World!")
def home(request):
    return HttpResponse("Bienvenue sur la page d'accueil!")

class ScrapListCreate(generics.ListCreateAPIView):
    queryset = Scrap.objects.all().select_related('owner')
    serializer_class = ScrapSerializer