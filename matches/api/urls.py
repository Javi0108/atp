from django.urls import path

from matches import views

app_name = 'matches'

urlpatterns = [
    path('matches/', views.MatchListView.as_view(), name='match_list'),
    path('matches/<pk>/', views.MatchDetailView.as_view(), name='match_detail'),
]
