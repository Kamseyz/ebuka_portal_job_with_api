"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #django allauth
    path('accounts/', include('allauth.urls')),
    
    #REST FRAMEWORKAPI
    path('api-auth/', include('rest_framework.urls')),
    
    #JOB API URL
    path('api/', include('jobboard.api_urls')),
    #JOB URL
    path('', include('jobboard.urls')),
    # WORKER API URL
    path('api/', include('workers.api_urls')),
    #WORKER URL
    path('', include('workers.urls')),
    #EMPLOYER 
    path('', include('employers.urls')),
    #EMPLOYER API URL
    path('api/', include('employers.api_urls')),
    #ACCOUNT URL
    path('', include('accounts.urls'))
    #ACCOUT API URL
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)