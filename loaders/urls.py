from django.urls import path

from . import views

app_name = 'loaders'
urlpatterns = [
    path('loaders/', views.get_datos, name='get_datos'),
]
