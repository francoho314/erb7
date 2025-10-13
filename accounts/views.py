from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == "POST" :
        print("submit")
        messages.success(request, 'Account created Successfully')
        #debug message content
        #storage = messages.get_messages(request)
        #for message in storage:
        #    print(message.level_tag, message.message)
        return redirect('accounts:register')
    else:
        return render (request, 'accounts/register.html')
    
def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return redirect(request, 'pages:index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
