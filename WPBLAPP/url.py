from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('index',views.DSA,name='index'),
    path('SADindex',views.SAD,name='SADindex'),
    path('New',views.new,name='new'),
    path('trans', views.handle_deposit, name='handle_deposit'),
    path('transSAD', views.handle_depositSAD, name='handle_depositSAD'),
    path('sad',views.SADAcc,name='saving'),
    path('admin1',views.admin1,name='admin1'),
    path('adminuser',views.adminuser,name='adminuser'),
    path('adminSAD',views.SADadmin,name='adminSAD')
]