from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Comment
from .serializers import CommentSerializer

class CommentViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    


    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context
