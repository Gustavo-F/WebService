from . import views
from django.urls import path


urlpatterns = [
    path('add_statistic/', views.add_statistic),
    path('get_statistics/', views.get_statistics),
    path('delete/<int:pk>', views.delete_stat),
    path('update/<int:pk>', views.update_stat),
]
