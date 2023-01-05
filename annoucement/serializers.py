from rest_framework.serializers import ModelSerializer
from .models import Annoucement_category, Annoucement

class AnnoucementSerializer(ModelSerializer):
    class Meta:
        model = Annoucement
        fields = ['id','user', 'title', 'description', 'category_name', 'created_at', 'annoucement_status']

class AnnoucementCategorySerializer(ModelSerializer):
    class Meta:
        model = Annoucement_category
        fields = ['id','category_name']





# class Annoucement_categorySerializer(serializers.models.ModelSerializer):
#     pass

