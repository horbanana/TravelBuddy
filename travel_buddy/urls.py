"""travel_buddy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from travel_buddy_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main', views.index),
    path('registration', views.registration),
    path('login', views.login),
    path('travels', views.success),
    path('logout', views.logout),
    path('travels/add', views.plan),
    path('planning', views.planning),
    path('travels/destination/<trip_id>', views.info),
    path('join/<trip_id>', views.join),
    # path('removeitem/<trip_id>',views.removeitem),
]

