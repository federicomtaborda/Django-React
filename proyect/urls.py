"""proyect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from apiblog.urls import router_blog


class DefaultRouter(routers.DefaultRouter):
    def extend(self, router):
        self.registry.extend(router.registry)


router = DefaultRouter()
router.extend(router_blog)

urlpatterns = [
    path('admin/', admin.site.urls),
    url('api/', include(router.urls)),
    url('api/docs', include_docs_urls(title='Blog Api', public=False)),
]
