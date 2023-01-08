from rest_framework import routers,serializers,viewsets
from .models import ProgramItem

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProgramItem
        fields = ['id', 'program_ID', 'program_date', 'program_data']


