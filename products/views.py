from django.http import HttpResponse
from rest_framework import generics,status
from rest_framework.response import Response
from .models import UserCustom,Scrap
from .serializers import ScrapSerializer

def index(request):
    return HttpResponse("Hello, World!")
def home(request):
    return HttpResponse("Bienvenue sur la page d'accueil!")

class ScrapListCreate(generics.ListCreateAPIView):
    queryset = Scrap.objects.all().select_related('owner')
    serializer_class = ScrapSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({
                "status": status.HTTP_201_CREATED,
                "message": "Produit créé avec succès.",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED, headers=headers)

        # Si le serializer est invalide, renvoyez les erreurs
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "Erreur lors de la création du produit.",
            "errors": serializer.errors,  # Voici les erreurs détaillées
            "data": request.data
        }, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        try:
            # Définir l'owner comme étant le premier utilisateur
            serializer.save(owner=UserCustom.objects.first())
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_400_BAD_REQUEST)