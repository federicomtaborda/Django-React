from django.urls import include
from django.conf.urls import url

from rest_framework import routers

from .views import CategoryViewSet, BlogViewSet

router_blog = routers.DefaultRouter()
router_blog.register(r'category', CategoryViewSet, basename='category'),
router_blog.register(r'blog', BlogViewSet, basename='blog'),

urlpatterns = [
    url('/', include(router_blog.urls)),
]