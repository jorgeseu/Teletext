from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Annoucement_category, Annoucement

class AnnoucementSerializer(ModelSerializer):
    #z with owner there works
    user = serializers.ReadOnlyField(source='user.name')

    class Meta:
        model = Annoucement
        fields = ['id','user', 'title', 'description', 'category_name', 'created_at', 'annoucement_status']

class AnnoucementCategorySerializer(ModelSerializer):
    class Meta:
        model = Annoucement_category
        fields = ['id','category_name']





# class Annoucement_categorySerializer(serializers.models.ModelSerializer):
#     pass

