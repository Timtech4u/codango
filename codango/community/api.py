from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from models import TimeStampMixin, Tag
from serializers import (TimeStampMixinSerializer, TagSerializer )
# Create your views here.

class TagAPIView(generics.ListCreateAPIView):
    """
    For api/v1/tag/ url path
    To enable  community members to make create and view tags
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = TagSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SingleTagAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    For api/v1/tag/id/ url path
    To enable  community members to make retrieveedit and delete tags
    """

    queryset = models.Tag.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = TagSerializer




