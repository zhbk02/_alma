from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProductViewSet, CategoryViewSet, CommentViewSet, add_rating, toggle_like

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('commnets', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]