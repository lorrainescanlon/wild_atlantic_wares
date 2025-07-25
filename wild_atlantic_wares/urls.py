"""wild_atlantic_wares URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('basket/', include('basket.urls')),
    path('checkout/', include('checkout.urls')),
    path('profiles/', include('profiles.urls')),
    path('about/', include('about.urls')),
    path('summernote/', include('django_summernote.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = 'wild_atlantic_wares.views.handler403'
handler404 = 'wild_atlantic_wares.views.handler404'
handler405 = 'wild_atlantic_wares.views.handler405'
handler500 = 'wild_atlantic_wares.views.handler500'
