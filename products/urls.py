from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('api/scraps/', views.ScrapListCreate.as_view(), name='scrap-list-create'),
    path('api/signup/', views.signup_api, name='signup-api'),
]