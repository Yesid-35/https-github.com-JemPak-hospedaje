"""reservas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from hospedaje import views

urlpatterns = [
    path("hospedaje", views.hospedajeDetails.as_view()),
    path("hospedaje/<int:pk>", views.hospedajeRetrieveUpdate.as_view()),
    path("filterByType/<int:type>", views.filterByTypeHospedaje.as_view()),
    path("filterByCity/<str:city>", views.filterBycity.as_view()),
]
