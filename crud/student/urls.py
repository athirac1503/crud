from django.urls import path
from. import views

urlpatterns=[
       
        path('student_login',views.student_login,name='student_login'),
        # path('reg',views.reg,name='reg'),
        path('student_list',views.student_list,name='student_list'),
        path('student_profile',views.student_profile,name='student_profile')

]