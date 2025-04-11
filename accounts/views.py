from django.shortcuts import render, redirect
from django.contrib import messages, auth
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .models import User
from django.contrib.auth.hashers import make_password


def admin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            auth_login(request, user)
            return redirect('admin_dashboard')  # Redirect to Django Admin Panel or custom admin dashboard
        else:
            messages.error(request, "Invalid credentials or not a superuser.")
    return render(request, 'accounts/admin.html')

def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(f"Attempting to authenticate user: {username}")

        user = auth.authenticate(user_name=username, password=password)  # Authenticate using username

        if user is not None:
            print(f"Authenticated user: {user}")
            auth.login(request, user)
            # messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            print("Authentication failed")
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')



def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(user_name=username).exists():  # Use `user_name` for your custom model
                messages.error(request, 'Username already exists!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('register')
                else:
                    # Create a new user using your custom User model
                    user = User.objects.create(
                        first_name=firstname,
                        last_name=lastname,
                        user_name=username,
                        email=email,
                        password=make_password(password)  # Note: Password should be hashed for security
                    )
                    user.save()

                    # Authenticate and log in the user
                    authenticated_user = auth.authenticate(user_name=username, password=password)
                    if authenticated_user is not None:
                        auth.login(request, authenticated_user)
                        messages.success(request, 'You are Successfully Registered Now logged in.')
                        return redirect('login')
                    else:
                        messages.error(request, 'User registered but could not be logged in. Please log in manually.')
                        return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def logout(request):
    if request.method == 'POST':
        # messages.clear(request)
        auth.logout(request)
        # messages.success(request, 'You are successfully logged out.')
        return redirect('home')
    return redirect('home')
