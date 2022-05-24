from django.shortcuts import render

from adminapp.models import StudentRegister
from django.shortcuts import redirect, render


# Create your views here.
def student_login(request):
    error_msg = ''
    if request.method == 'POST':
        user_name = request.POST['user_std']
        std_password = request.POST['pass_std']
        seller_data = StudentRegister.objects.filter(
            username=user_name, password=std_password).exists()
        if seller_data:
            seller=StudentRegister.objects.get(username=user_name,password=std_password)
            request.session['student_id']=seller.id
            return redirect('student_profile')
        else:
            error_msg = "Invalid user name and password"
    return render(request, 'student_app/student_login.html',{'error': error_msg})

def student_list(request):
    return render(request, 'student_app/student_list.html')

def student_profile(request):
    current_user=request.session['student_id']
    profile=StudentRegister.objects.get(id=current_user)
    return render(request, 'student_app/student_profile.html',{'prof':profile})