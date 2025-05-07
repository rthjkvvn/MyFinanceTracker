from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .models import Transaction


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
            #vuid = request.POST['uid']
            vusername = request.POST['username']
            vemail = request.POST['email']
            vpassword = request.POST['password']
            # Check if user ID already exists
            if User.objects.filter(username=vusername).exists():
                messages.error(request, 'User with this Name already exists!')
                return redirect('userreg')
                
            # Create and save new user
            user=User(username=vusername, email=vemail) 
                                
            user.set_password(vpassword)
            user.save()
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
    x = User.objects.filter(id=id)
    x.delete()
    return redirect("/userlist")

def useredit(request, id):
    y = User.objects.get(id=id)
    return render(request,"dashboard/useredit.html", {'user':y})

def updateprofile(request, id):
    if request.method=='POST':
        try:
            user=User.objects.get(id=id)

            user.username = request.POST['username']
            user.email = request.POST['email']
            new_password = request.POST.get('password')
            if new_password:
                user.set_password(new_password)

            user.save()
            messages.success(request, 'Successfully Updated')
            return redirect('/userlist')
        except User.DoesNotExist:
            messages.error(request, 'User not found')
            return redirect('/userlist')
        except Exception as e:
            messages.error(request, f'Error in updating: {str(e)}')
            return redirect('/userlist')
        
    return redirect('/userlist')

def transaction(request):
        return render(request, 'dashboard/transaction.html')

def viewtransaction(request):
    transaction = Transaction.objects.all()
    return render(request, "dashboard/viewtransaction.html", {'transactiondata' : transaction})


def categoryreg(request):
    return render(request, 'dashboard/categoryreg.html', {}) 


