from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html')

# dashboard/views.py
def users(request):
    users = User.objects.all().order_by('-id')  # Get all users ordered by newest first
    return render(request, 'dashboard/users.html', {'users': users})
def transaction(request):
    return render(request, 'dashboard/transaction.html')

def category(request):
    return render(request, 'dashboard/category.html')

def userreg(request):
    return render(request, 'dashboard/userreg.html', {})


def insertuser(request):
    if request.method == 'POST':
        try:
            vuid = request.POST['uid']
            vusername = request.POST['username']
            vemail = request.POST['email']
            
            # Check if user ID already exists
            if User.objects.filter(uid=vuid).exists():
                messages.error(request, 'User with this ID already exists!')
                return redirect('userreg')
                
            # Create and save new user
            User.objects.create(uid=vuid, username=vusername, email=vemail)
            messages.success(request, 'User registered successfully!')
            return redirect('dashboard-users')
            
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
            return redirect('userreg')
    
    return redirect('userreg')

def userlist(request):
    user = User.objects.all()
    return render(request, "dashboard/userlist.html",{'users': user})

def deleteprofile(request, id):
    x = User.objects.filter(uid=id)
    x.delete()
    return redirect("/userlist")

def useredit(request, id):
    y = User.objects.get(uid=id)
    return render(request,"dashboard/useredit.html", {'user':y})

def updateprofile(request, id):
    newuid=request.POST['uid']
    newusername=request.POST['username']
    newemail=request.POST['email']
    user=User.objects.get(uid=id)
    user.uid=newuid
    user.username=newusername
    user.email=newemail
    user.save()
    return redirect("/userlist")
