from rest_framework import serializers
from models import *

class TimeStampMixinSerializer(serializers.ModelSerializer):
    """TimeStampMixin Serializer"""

    class Meta:
        model = TimeStampMixin
        fields = ('id',  'date_created', 'date_modified')

        read_only_fields = ('date_created', 'date_modified')

class TagSerializer(serializers.ModelSerializer):
    """Tag Serializer"""

    class Meta:
        model = Tag
        fields = ('id', 'title', 'date_created', 'date_modified')

        read_only_fields = ('date_created', 'date_modified')
