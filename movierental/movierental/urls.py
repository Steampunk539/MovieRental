"""movierental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', views.MovieList.as_view()),
    path('movies/<uuid:pk>/', views.MovieDetail.as_view()),
    path('movietype/', views.MovieTypeList.as_view()),
    path('movietype/<uuid:pk>/', views.MovieTypeDetail.as_view()),
    path('author/', views.AuthorList.as_view()),
    path('author/<uuid:pk>/', views.AuthorDetail.as_view()),
    path('movies/rent/<uuid:pk>/', views.RentMovie.as_view()),
    path('movies/return/<uuid:pk>/', views.ReturnMovie.as_view()),
]
