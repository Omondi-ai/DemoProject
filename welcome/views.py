from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'welcome/index.html')

def register(request):
    form = CreateUserForm()
    context = {'RegisterForm': form}  # Initialize context here

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save() 
            return redirect('my-login')
            return HttpResponse('User Registered')
           

    return render(request, 'welcome/register.html', context)


def my_login(request):
    form = AuthenticationForm()
    context = {'loginForm': form}

    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
#username/email
            user = authenticate(request, username=username, password=password)

            if user is user.is_teacher  == True :

                if user.is_teacher != True:
                    login(request, user)

                    return redirect('my-login')

                login(request, user)

                return redirect('teacher-dashboard')

                
            elif user is not None and user.is_parent == True:

                login(request, user)
    
                return redirect('parent-dashboard')


            elif user is not None and user.is_student  == True:

                login(request, user)

                return redirect('student-dashboard')

            elif user is not None and user.is_parent  and user.is_student and user.is_teacher == False:

                login(request, user)
    
                return redirect('my-login')
            
           
    context = {'LoginForm': form}



    return render(request, 'welcome/my-login.html', context)


def user_logout(request):
    logout(request)
    return redirect("my-login")
