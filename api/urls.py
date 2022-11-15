from django.urls import path
from. import views

urlpatterns = [

    path('', views.home, name='home'),
    path('student/<str:pk>/', views.studentlist, name='studentlist'),
    path('studentadd/', views.addstudent, name='addstudent'),
    path('studentupdate/<str:pk>/', views.updatestudent, name='updatestdent'),
    path('studentdelete/<str:pk>/', views.deletestudent, name='deletestudent'),

]
