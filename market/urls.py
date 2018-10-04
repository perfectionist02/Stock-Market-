from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url(r'^homepage/', views.homepage, name='homepage'),
    url(r'^stocks', views.stocks, name='stocks'),
    url(r'^login/',views.loginaction, name='login'),
    url(r'^register/',views.register,name='register'),
    url(r'^portfolio/',views.portfolio,name='portfolio'),
    url(r'^transact/',views.transact,name='transact'),
    url(r'^logout/',views.logoutaction,name='logout'),
    
]

