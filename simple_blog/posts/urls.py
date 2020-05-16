from django.urls import path

from . import views

urlpatterns =[
    path('', views.PostListsView.as_view(), name='index'),
]
