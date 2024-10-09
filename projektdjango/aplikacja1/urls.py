from django.urls import path, include
from .views import index,store

urlpatterns = [
    path('employees/', index, name='index'),
    path('store/<int:id>/', store, name='store')
]