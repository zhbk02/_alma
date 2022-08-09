from rest_framework.viewsets import ModelViewSet, GenericViewSet

from rest_framework import mixins

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Product, Category
from .serializer import ProductSerializer, CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

        
        
        
class CategoryViewSet(mixins.CreateModelMixin, 
                     mixins.DestroyModelMixin, 
                     mixins.ListModelMixin, 
                     GenericViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
