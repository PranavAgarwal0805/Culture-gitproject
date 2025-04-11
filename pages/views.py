
from django.shortcuts import render, redirect
from .models import User, MembershipApplication
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views import View
from .models import MembershipApplication
from .models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def membership(request):
    return render(request, 'pages/membership.html')
# def profile(request):
#     return render(request, 'pages/profile.html')

@login_required
def profile(request):
    user = request.user

    if request.method == 'POST':
        user.interest = request.POST.get('interest', '')
        user.address = request.POST.get('address', '')
        user.phone_no = request.POST.get('phone_no', '')
        user.save()
        return redirect('profile')

    return render(request, 'pages/profile.html', {'user': user})


def status(request):
    application = MembershipApplication.objects.filter(user=request.user).first()
    return render(request, 'pages/status.html', {'application': application})



@login_required
def application(request):
    user = request.user  # Get the logged-in user
# Get the membership type from the query parameter
    membership_type = request.GET.get('type')
    # Check if the user has already applied for membership
    if MembershipApplication.objects.filter(user=user).exists():
        messages.info(request, "You have already submitted the application.")
        return render(request, 'pages/application.html', {'already_applied': True})

    if request.method == 'POST':
        data = request.POST

        # Create a new membership application
        MembershipApplication.objects.create(
            user=user,
            membership_type=membership_type,
            current_interest=data.get('current_interest'),
            hobbies_passions=data.get('hobbies_passions'),
            join_reason=data.get('join_reason'),
            contribution_method=data.get('contribution_method'),
            member_goals=data.get('member_goals'),
            participation_frequency=data.get('participation_frequency'),
            accessibility_needs=data.get('accessibility_needs'),
            wants_newsletter=(data.get('wants_newsletter') == 'True'),
            passionate_causes=data.get('passionate_causes'),
            event_ideas=data.get('event_ideas'),
            previous_projects=data.get('previous_projects'),
            six_month_contribution=data.get('six_month_contribution'),
        )

        messages.success(request, "Application submitted successfully.")
        return render(request, 'pages/application.html', {'already_applied': True})
        # return redirect('dashboard')  # Redirect to the dashboard or another page

    return render(request, 'pages/application.html')
