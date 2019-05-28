"""festival URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

import festivalapp.views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', festivalapp.views.home, name='home'),
    path('programmerintro/', festivalapp.views.programmerintro, name='programmerintro'),
    path('pubintro/<int:pk>', festivalapp.views.pubintro, name='pubintro'),
    path('shareboard/', festivalapp.views.shareboard, name='shareboard'),
    path('newboard/', festivalapp.views.newboard, name='newboard'),
    path('finishboard/<int:pk>', festivalapp.views.finishboard, name='finishboard'),
    path('detailboard/', festivalapp.views.detailboard, name='detailboard'),
    path('writingarea/', festivalapp.views.writingarea, name='writingarea'),
    path('writingpw/', festivalapp.views.writingpw, name='writingpw'),
    path('writingcheck/', festivalapp.views.writingcheck, name='writingcheck'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


