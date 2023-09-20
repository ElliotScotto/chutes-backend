from rest_framework import serializers
from .models import UserCustom, Scrap

class UserCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustom
        fields = ('username', 'email', 'phone_number','address','city')

class ScrapSerializer(serializers.ModelSerializer):
    owner=UserCustomSerializer()

    class Meta:
        model = Scrap
        fields = '__all__' 