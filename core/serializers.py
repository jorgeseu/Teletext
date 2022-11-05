from rest_framework import routers,serializers,viewset
from frontend.models import ProgramItem

class TaskSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProgramItem
        fields = ['id', 'program_ID', 'program_date', 'program_data']