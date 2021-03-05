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
from django.urls import path, reverse_lazy

from core.views import Index, landing, legal

from users.views import (RegisterView, CustomLoginView,
                         CustomLogoutView, UserSettingsView, ProfileView)

from match.views import (CreateMatchView, UpdateMatchView, MatchPlannedListView, MatchInProgressListView, MatchOverListView,
                         MatchDetailView, MatchSubscriptionListView,
                         cancel_match, kick_player)

from search_manager.views import (SearchMapMatchView, SearchTableMatchView,
                                  SearchMapPlayerView)
from search_manager.ajax_view import (filter_match_view, filter_player_view, autocomplete_city,
                                      get_user_current_coordinates,
                                      autocomplete_player)

from player.views import (PlayerInvitationListView, cancel_match_request,
                          decline_match_invitation, accept_match_invitation)

from player.ajax_view import (player_follow)

from notifications.views import (NotificationListView, delete_notification)

from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView)

urlpatterns = [
    path('', landing, name='landing'),
    path('legal/', legal, name='legal'),
    path('admin/', admin.site.urls),
    path('index/', Index.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('password-reset/', PasswordResetView.as_view(
        template_name='users/reset_password.html'), name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(
        template_name='users/reset_password_done.html'), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='users/reset_password_confirm.html'), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(
         template_name='users/reset_password_complete.html'), name='password_reset_complete'),
    path('profile/<slug:username>', ProfileView.as_view(), name='profile'),
    path('settings/profile', UserSettingsView.as_view(), name='settings-profile'),
    path('match/create/', CreateMatchView.as_view(), name='match-creation'),
    path('match/update/<int:pk>', UpdateMatchView.as_view(), name='match-update'),
    path('match/list/planned', MatchPlannedListView.as_view(), name='match-planned'),
    path('match/list/over', MatchOverListView.as_view(), name='match-over'),
    path('match/list/in-progress', MatchInProgressListView.as_view(),
         name='match-in-progress'),
    path('match/subscription/', MatchSubscriptionListView.as_view(),
         name='match-subscription'),
    path('match/detail/<int:pk>/', MatchDetailView.as_view(), name='match-detail'),
    path('search/map/match/', SearchMapMatchView.as_view(), name='search-map-match'),
    path('search/table/match/', SearchTableMatchView.as_view(),
         name='search-table-match'),
    path('search/map/player/', SearchMapPlayerView.as_view(),
         name='search-map-player'),
    path('search/match/filter', filter_match_view, name='filter-match'),
    path('search/match/player', filter_player_view, name='filter-player'),
    path('autocomplete', autocomplete_city, name='city-autocomplete'),
    path('player-autocomplete', autocomplete_player, name='player-autocomplete'),
    path('player/follow', player_follow, name='player-follow'),
    path('current_coordinates', get_user_current_coordinates,
         name='current-coordinates'),
    path('player/invitations/', PlayerInvitationListView.as_view(),
         name='player-invitations'),
    path('cancel_match_request/<int:pk>/',
         cancel_match_request, name='cancel-match-request'),
    path('decline_match_invitation/<int:pk>/', decline_match_invitation,
         name='decline-match-invitation'),
    path('accept_match_invitation/<int:pk>/', accept_match_invitation,
         name='accept-match-invitation'),
    path('cancel_match/<int:pk>/', cancel_match,
         name='cancel-match'),
    path('remove-player/<int:pk>/', kick_player, name='remove-player'),
    path('notifications/', NotificationListView.as_view(),
         name='notifications'),
    path('notifications/delete/<int:pk>',
         delete_notification, name='delete-notification'),
]

handler404 = 'core.views.custom_page_not_found_view'
