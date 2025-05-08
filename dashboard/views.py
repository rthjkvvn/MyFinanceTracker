from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from .models import User
from .models import Transaction
from .models import Category1
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404


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

    search_query = request.GET.get('search', '')
    if search_query:
        user = User.objects.filter(username__icontains=search_query)
    else:
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

def userreg(request):
    return render(request, 'dashboard/userreg.html', {})

def categoryreg(request):
    return render(request, 'dashboard/categoryreg.html', {}) 

    return render(request, "dashboard/userlist.html",{'users': user})

def insertcategory(request):
    if request.method == 'POST':
        vcname = request.POST[ 'cname' ]
        vcset_budget = request.POST[ 'cset_budget']
        vcspend = request.POST[ 'cspend' ]
        vcusername = request.POST[ 'cusername' ]
        if Category1.objects.filter(cname=vcname).exists():
            messages.error(request, 'Category with this Name already exists!')
            return redirect('categoryreg')
        
        cat=Category1(cname=vcname, cset_budget=vcset_budget, cspend=vcspend, cusername=vcusername)
        cat.save()
        messages.success(request, 'Category registered successfully!')
        return redirect('dashboard-category')


def categorylist(request):
    cat=Category1.objects.all()
    return render(request, 'dashboard/categorylist.html', {'category':cat})

def updatecategory(request, id):
    if request.method=='POST':
        try:
            cat=Category1.objects.get(id=id)
            cat.cname= request.POST['cname']
            cat.cset_budget = request.POST['cset_budget']
            cat.cspend = request.POST['cspend']
            cat.cusername = request.POST['cusername']
            cat.save()
            return redirect('/categorylist')
        
        except Category1.DoesNotExist:
            messages.error('Category not found')
            return redirect(request, '/categorylist')
            
    return redirect('/categorylist')

def categoryedit(request, id):
    z = Category1.objects.get(id=id)
    return render(request,"dashboard/categoryedit.html", {'category' : z})

    


