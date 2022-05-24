from django.shortcuts import render

from adminapp.models import StudentRegister

# Create your views here.
def admin_login(request):
    return render(request,'admin_app/admin_login.html')
def student_register(request):
    if request.method=='POST':
        std_name=request.POST['stu_name']
        std_contact=request.POST['stu_contact']
        std_email=request.POST['stu_email']
        std_username=request.POST['stu_user']
        std_password=request.POST['stu_pass']
        obj=StudentRegister(name=std_name,contact=std_contact,email=std_email,username=std_username,password=std_password)
        obj.save()
    return render(request, 'admin_app/student_register.html')
def dashboard(request):
    return render(request, 'admin_app/dashboard.html')
def view_student(request):
    return render(request, 'admin_app/view_student.html')