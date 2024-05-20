from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, LoginForm, ProfileForm


def signupuser(request):
    """
    Handle user registration.
    If POST request, processes form data to register a new user. Redirects to
    index page upon successful registration.
    If GET request, displays the registration form.
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:index')
        else:
            return render(request, 'users/signup.html',
                          context={"form": form})

    return render(request, 'users/signup.html',
                  context={"form": RegisterForm()})


def loginuser(request):
    """
    Handle user login.
    If POST request, authenticates user. If authentication fails,
    returns to login page with an error message. If successful,
    redirects to the index page.
    """
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect(to='users:login')

        login(request, user)
        return redirect(to='quotesapp:index')

    return render(request, 'users/login.html', context={"form": LoginForm()})


@login_required
def logoutuser(request):
    """
    Log out the current user and redirect to the index page.
    """
    logout(request)
    return redirect(to='quotesapp:index')


@login_required
def profile(request):
    """
    Handle user profile updates.
    If POST request, processes form data to update user's profile.
    If successful, redirects to the profile page with a success message.
    If GET request, displays the user's profile form.
    """
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users:profile')

    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/profile.html',
                  {'profile_form': profile_form})
