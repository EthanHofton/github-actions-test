from django.urls import path

from . import views

app_name = 'shopping_list'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:itemId>/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
    path('view/', views.view, name='view'),
]
