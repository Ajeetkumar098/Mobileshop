"""mobile_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from mobile_app import views

admin.site.site_header = "Ajeet Kumar Admin"
admin.site.site_title = "Mobile Shop Admin Portal"
admin.site.index_title = " Welcome to Mobile Shop Admin"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('login',views.login,name='login'),
    path('show',views.show,name='show'),
    path('form',views.form,name='form'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('readmore<int:id>',views.readmore,name='readmore'),
    path('service/<str:service1>',views.service_fil,name='service'),
    path('contact',views.contact,name='contact'),
    path('profile',views.profile,name='profile'),
    path('changep',views.changep,name='changep'),
    path('profileimage',views.profile_image,name='profileimage'),
    path('update<int:id>',views.update,name='update'),
    path('readmore_two<int:id>',views.readmore_two,name='readmore_two'),
    path('types/<str:types1>',views.types_fil,name='types'),
    path('show_two',views.show_two,name='show_two'),


]
