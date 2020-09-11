from django.urls import path
from . import views

app_name = 'museum'
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('ship',views.shi,name='shi'),
    path('info',views.info,name='info'),
    path('add',views.add,name = 'add'),
    path('myfun',views.myfun,name='myfun'),
    path('select_ship',views.ship_data, name='select_ship'),
    path('index',views.index, name='index'),
    path("register/", views.register, name="register"),
    path('logout_request', views.logout_request, name='logout_request'),
    path('login_request', views.login_request, name='login_request'),
    path('photos_gallery',views.photos_gallery, name='photos_gallery')
]