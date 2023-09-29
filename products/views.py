import logging
from django.http import HttpResponse
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .models import UserCustom,Scrap
from .serializers import ScrapSerializer
from django.core.files.uploadedfile import UploadedFile


logger = logging.getLogger(__name__)

def index(request):
    return HttpResponse("Hello, World!")
def home(request):
    return HttpResponse("Bienvenue sur la page d'accueil!")

class ScrapListCreate(generics.ListCreateAPIView):
    queryset = Scrap.objects.all().select_related('owner')
    serializer_class = ScrapSerializer
    parser_classes = (MultiPartParser,)

    def post(self, request, *args, **kwargs):
        logger.debug("Starting POST method")

        serializer = self.get_serializer(data=request.data)
        logger.debug("Serializer initialized with request data")
        # Afficher le contenu de request.data
        print("request.data:", request.data)
    
        # Afficher les fichiers inclus dans la requête
        print("request.FILES:", request.FILES)
        if serializer.is_valid():
            logger.debug("Serializer is valid")

            self.perform_create(serializer)
            logger.debug("Object created with serializer")

            headers = self.get_success_headers(serializer.data)
            return Response({
                "status": status.HTTP_201_CREATED,
                "message": "Produit créé avec succès.",
            }, status=status.HTTP_201_CREATED, headers=headers)
        else:
            logger.error("Serializer is not valid. Errors: %s", serializer.errors)
        # Si le serializer est invalide, renvoyez les erreurs
        return Response({
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "Erreur lors de la création du produit.",
            "errors": serializer.errors,  # Voici les erreurs détaillées
        }, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        try:
            # Définir l'owner comme étant le premier utilisateur
            scrap=serializer.save(owner=UserCustom.objects.first(), commit=False)
            scrap.photo1 = self.request.FILES.get('photo1')
            scrap.save()
        except Exception as e:
            logger.error("Error in perform_create: %s", str(e))
            raise e  # re-raise the exception to handle it in the calling function (e.g., post method)