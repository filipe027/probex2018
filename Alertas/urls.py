from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:loc>&<str:data>&<int:valor_med>&<str:senha>', views.upload, name='upload_database'),
    path('<str:loc>&<int:valor_med>&<str:senha>', views.upload_server_date, name='upload_server_date')
]