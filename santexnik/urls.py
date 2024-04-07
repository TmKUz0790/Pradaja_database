from django.contrib import admin
from django.urls import path
from santexnik import views


urlpatterns = [
   path('', views.santexnik_list, name='santexnik-list'),
    path('add_santexnik/', views.add_santexnik, name='add-santexnik'),
    path('edit_santexnik/<int:pk>/', views.edit_santexnik, name='edit-santexnik'),
    path('delete_santexnik/<int:pk>/', views.delete_santexnik, name='delete-santexnik'),

    ]