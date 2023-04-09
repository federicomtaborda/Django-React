from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .serializers import BlogSerialezer, CategorySerialezer
from .models import Blog, Category


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 100


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerialezer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        '''
           recibe parametro ? search
        '''
        search = self.request.query_params.get('search', None)
        queryset = Blog.objects.all()
        if search:
            queryset = queryset.filter(description__icontains=search)
        return queryset



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerialezer