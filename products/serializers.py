from rest_framework import serializers
from .models import UserCustom, Scrap

class UserCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCustom
        fields = ('username', 'email', 'phone_number','address','city')

class ScrapSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=UserCustom.objects.all())
    owner_detail = UserCustomSerializer(source='owner', read_only=True)

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
        fields = ('id', 'owner', 'owner_detail', 'photo1', 'photo2', 'photo3', 'photo4', 'photo5', 'name', 'description', 'condition', 'price', 'weight', 'material', 'category', 'home_pickup', 'product_location', 'created_at')