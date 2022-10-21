from django.urls import path
from .views import send_request
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('signin/', views.login_page, name='signin'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('user/', views.User_page, name='user_page'),
    path('send_request/', views.send_request, name='send_request'),
    path('my_appointment/', views.my_appointment, name='my_appointment'),
    path('dashboard/', views.dashboard, name='dashboard'),
 path('patient/<str:pk_test>/', views.patient, name="patient"),

]
