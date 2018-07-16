from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:n_med>', views.latest_med, name='latest_medicao')
]