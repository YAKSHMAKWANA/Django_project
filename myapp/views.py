from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')



def login(request):
    if request.method == 'POST':
        un = request.POST['uname']
        p1 = request.POST['Pass1']

        user = auth.authenticate(username=un, password=p1)

        print("------------------------------------------")

        if user is not None:
            auth.login(request, user)
            print('Login successfully!')  
            return redirect('/')
        else:
            print('Invalid username or password!!')   
            return redirect('/login/')  

    return render(request, 'login.html')



def contact(request):
    return render(request,'contact.html')

def register(request):
    if request.method == 'POST':
        fn = request.POST['fname']
        ln = request.POST['lname']
        em = request.POST['email']
        un = request.POST['uname']
        p1 = request.POST['pass1']
        p2 = request.POST['pass2']

        print("VALUES:", fn, ln, em, un, p1, p2)

        if p1 != p2:
            print("Password not matching!")
            return redirect('/register/')

        # Check username already exists
        if User.objects.filter(username=un).exists():
            print("Username already exists!")
            return redirect('/register/')

        # Create user
        user = User.objects.create_user(
            first_name=fn,
            last_name=ln,
            username=un,
            email=em,
            password=p1
        )
        user.save()

        print("User created successfully!")
        return redirect('/login/')  # ✔ After register → go to login page

    return render(request, 'register.html')




def logout(request):
    auth.logout(request)
    print('Logout successfully!')
    return redirect('/')

# def register(request):
#     return render(request,'register.html')

def tour(request):
    return render(request,'tour.html')

def tourlist(request):
    return render(request,'tour-list.html')


def destination(request):
    return render(request,'destination.html')

def blog(request):
    return render(request,'blog.html')