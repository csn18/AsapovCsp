from django.urls import path

from Main.views import cadets_list, cadet_detail

urlpatterns = [
    path('', cadets_list, name='cadets_list'),
    path('<int:pk>/', cadet_detail, name='cadet_detail'),
]
