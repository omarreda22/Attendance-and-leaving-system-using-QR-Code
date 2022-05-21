from email import message
from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        number_id = request.POST['number_id']
        password = request.POST['password']

        user = auth.authenticate(email=email, nubrer_id=number_id, password=password)
        if user is not None and user.nubmer_id == number_id:
            auth.login(request, user)
            return redirect('home:home')
        else:
            messages.warning(request, 'Information Login Incorrect.')
            return redirect('accounts:login')
    context={
        
    }
    return render(request, 'accounts/login.html', context)

@login_required(login_url = 'accounts:login')
def logout(request):
    auth.logout(request)
    messages.success(request, "You've successfully logged out!")
    return redirect('accounts:login')