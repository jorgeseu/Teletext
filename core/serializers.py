from rest_framework import routers,serializers,viewsets
from .models import
from mod_models import MOD_item
from stat import Stat_item

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProgramItem
        fields = ['id', 'program_ID', 'program_date', 'program_data']


class MODSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MOD_item
        fields = ['id', 'message_ID', 'message_date', 'message_content']

class StatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stat_item
        fields = ['id', 'stat_ID', 'stat_message', 'stat_user', 'stat_datetime']