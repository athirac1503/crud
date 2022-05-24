from django.urls import path
from. import views

urlpatterns=[
       
        path('admin_login',views.admin_login,name='admin_login'),
        path('student_register',views.student_register,name='student_register'),
        path('dashboard',views.dashboard,name='dashboard'),
        path('view_student',views.view_student,name='view_student'),


]