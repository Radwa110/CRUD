from django.contrib import admin
from django.urls import path

from django import views 
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('list',views.list,name="list"),
    path('add',views.add,name="add"),
    path('update',views.update,name="update"),
    path('eliminate',views.eliminate,name="eliminate"),
]

