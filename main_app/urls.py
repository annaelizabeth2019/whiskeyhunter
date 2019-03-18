from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('whiskey/', views.whiskey_index, name='index'),
    path('whiskey/<int:whiskey_id>/', views.whiskey_detail, name='detail'),
    path('whiskey/<int:pk>/update/', views.WhiskeyUpdate.as_view(), name='whiskey_update'),
    path('whiskey/<int:pk>/delete/', views.WhiskeyDelete.as_view(), name='whiskey_delete'),
    path('whiskey/create/', views.WhiskeyCreate.as_view(), name='whiskey_create'),
    path('whiskey/<int:whiskey_id>/add_tasting/', views.add_tasting, name='add_tasting'), 
]