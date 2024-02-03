from django.urls import path

from players import views

app_name = 'players'

urlpatterns = [
    path('players/', views.PlayerListView.as_view(), name='player_list'),
    path('players/<pk>/', views.PlayerDetailView.as_view(), name='player_detail'),
]
