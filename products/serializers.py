from rest_framework import serializers
from .models import UserCustom, Scrap
from django.conf import settings

class UserCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustom
        fields = ('username', 'email', 'phone_number','address','city')

class ScrapSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=UserCustom.objects.all())
    owner_detail = UserCustomSerializer(source='owner', read_only=True)

    photo1_url = serializers.SerializerMethodField()
    photo2_url = serializers.SerializerMethodField()
    photo3_url = serializers.SerializerMethodField()
    photo4_url = serializers.SerializerMethodField()
    photo5_url = serializers.SerializerMethodField()

    def get_photo1_url(self, obj):
        print("get_photo1_url 1")
        if obj.photo1:
            print("get_photo1_url 2")
            return settings.MEDIA_URL + str(obj.photo1)
        return None
    def get_photo2_url(self, obj):
        if obj.photo2:
            return settings.MEDIA_URL + str(obj.photo2)
        return None
    def get_photo3_url(self, obj):
        if obj.photo3:
            return settings.MEDIA_URL + str(obj.photo3)
        return None
    def get_photo4_url(self, obj):
        if obj.photo4:
            return settings.MEDIA_URL + str(obj.photo4)
        return None
    def get_photo5_url(self, obj):
        if obj.photo5:
            return settings.MEDIA_URL + str(obj.photo5)
        return None
    
    def validate_material(self, value):
        if len(value) > 2:
            raise serializers.ValidationError("Vous ne pouvez sélectionner que 2 matériaux au maximum.")
        for material in value:
            if material not in [choice[0] for choice in Scrap.MATERIAL_CHOICES]:
                raise serializers.ValidationError(f"'{material}' n'est pas un choix valide.")
        return value

    def validate_category(self, value):
        if len(value) > 2:
            raise serializers.ValidationError("Vous ne pouvez sélectionner que 2 catégories au maximum.")
        for category in value:
            if category not in [choice[0] for choice in Scrap.CATEGORY_CHOICES]:
                raise serializers.ValidationError(f"'{category}' n'est pas un choix valide.")
        return value

    class Meta:
        model = Scrap
        fields = ('id', 'owner', 'owner_detail', 'photo1_url', 'photo2_url', 'photo3_url', 'photo4_url', 'photo5_url', 'name', 'description', 'condition', 'price', 'weight', 'material', 'category', 'home_pickup', 'sending', 'created_at')