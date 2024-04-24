from django.shortcuts import render,redirect

from django.http import HttpResponse

from django.contrib.auth.decorators import login_required


from teacher.models import Article

from student.models import Articlee

from . models import Parent


from welcome.models import CustomUser


from .forms import UpdateUserForm


@login_required(login_url='my-login')
def parent_dashboard(request):
    
    return render(request, 'parent/parent-dashboard.html')


@login_required(login_url='my-login')
def browse_articles(request):   

    articles = Article.objects.all()
    articlees = Articlee.objects.all()
    

    context = {'AllArticles': articles, 'AllArticlees': articlees}

    return render(request, 'parent/browse-articles4.html', context)
    


@login_required(login_url='my-login')
def account_management(request):
    try:
# updating account details

        form = UpdateUserForm(instance=request.user)

        if request.method == 'POST':

            form = UpdateUserForm(request.POST, instance=request.user)

            if form.is_valid():

                form.save()

                return redirect('parent-dashboard')

        context = { 'UpdateUserForm': form}

        return render(request, 'parent/account-management4.html', context)


    except:
            form = UpdateUserForm(instance=request.user)

            if request.method == 'POST':

                form = UpdateUserForm(request.POST, instance=request.user)

                if form.is_valid():

                    form.save()

                    return redirect('parent-dashboard')

    context = { 'UpdateUserForm': form}

    return render(request, 'parent/account-management4.html', context)
  


@login_required(login_url='my-login')
def delete_account(request):
    if request.method == 'POST':
        deleteUser = CustomUser.objects.get(email=request.user)

        deleteUser.delete()

        return redirect('')

    return render(request, 'parent/delete-account4.html')
    

