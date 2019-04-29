"""marvel URL Configuration

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
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view(), name='index_view'),
    url(r'^groups$', views.GroupsView.as_view(), name='groups_view'),
    url(r'^search/characters/$', views.SearchCharactersView.as_view(), name='search_characters'),
    url(r'^search/groups/$', views.SearchGroupsView.as_view(), name='search_groups'),
    url(r'^characters/(?P<pk>[0-9]+)/profile/$', views.CharacterDetailsView.as_view(), name='specific_character_profile'),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
