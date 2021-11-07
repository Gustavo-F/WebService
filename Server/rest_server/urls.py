from . import views
from django.urls import path


urlpatterns = [
    path('add_statistic/', views.add_statistic),
    path('get_statistics/', views.get_statistics),
]
