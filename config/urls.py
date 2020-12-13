"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from core.views import index

from users.views import RegisterView
from users.views import CustomLoginView, CustomLogoutView
from users.views import UserSettingsView

from match.views import CreateMatchView, MatchListView, MatchDetailView

from search_manager.views import SearchMapMatchView, SearchTableMatchView
from search_manager.ajax_view import (filter_match_view, autocomplete_city,
                                      get_user_current_coordinates)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('settings/profile/', UserSettingsView.as_view(), name='settings-profile'),
    path('match/create/', CreateMatchView.as_view(), name='match-creation'),
    path('match/list/', MatchListView.as_view(), name='match-list'),
    path('match/detail/<int:id>', MatchDetailView.as_view(), name='match-detail'),
    path('search/match/', SearchMapMatchView.as_view(), name='search-map-match'),
    path('search/table/match/', SearchTableMatchView.as_view(), name='search-table-match'),
    path('search/match/filter', filter_match_view, name='filter-match'),
    path('autocomplete', autocomplete_city, name='city-autocomplete'),
    path('current_coordinates', get_user_current_coordinates,
         name='current-coordinates')
]


handler404 = 'core.views.custom_page_not_found_view'
