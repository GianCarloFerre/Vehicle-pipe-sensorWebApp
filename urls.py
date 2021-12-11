from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='MVNS-index'),
    path('login/', views.login, name='MVNS-login'),
    path('view/', views.view, name='MVNS-view'),
    path('add-data/', views.add_data, name='MVNS-add-data'),
    path('edit-data/<int:pk>/', views.edit_data, name='MVNS-edit-data'),
]
