from rest_framework import serializers

from .models import Product, Category
from comments.serializers import CommentSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'




    def to_representation(self, instance:Product ):
        rep = super().to_representation(instance)
        rep['comments'] = CommentSerializer(instance.comments.all(), many = True).data
        return rep 


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =  Category
        fields = '__all__'