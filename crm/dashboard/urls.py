from django.urls import path, include

from crm.dashboard import views

urlpatterns = [

    path('', views.register,name= 'reg'),
    path('CRM_login', views.login_view,name='login'),
]