from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import RegisterForm, LoginForm, ProfileForm
from smtplib import SMTPException


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


class CustomPasswordResetView(SuccessMessageMixin, PasswordResetView):
    """
    Handle user password reset requests.
    Extends Django's PasswordResetView to include email validation.

    Attributes:
        template_name (str): Template for the password reset page.
        email_template_name (str): Template for the email text body.
        html_email_template_name (str): Template for the email HTML body.
        success_url (str): URL to redirect to after successful email send.
        success_message (str): Success message to display after email send.
        subject_template_name (str): Template for the email subject.

    Methods:
        form_valid(form):
            Validates the form and sends the password reset email
            if the user exists. Displays an error message if email sending
            fails or the email is not registered.
    """
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    html_email_template_name = 'users/password_reset_email.html'
    success_url = reverse_lazy('users:password_reset_done')
    success_message = ("An email with instructions to reset your password "
                       "has been sent to %(email)s.")
    subject_template_name = 'users/password_reset_subject.txt'

    def form_valid(self, form):
        """
        Validate the form and send password reset email if the user exists.

        Args:
            form (PasswordResetForm): Form instance with cleaned data.

        Returns:
            HttpResponse: Redirect to success URL if email is sent
                          successfully, else redirect back to the password
                          reset page with an error message.
        """
        email = form.cleaned_data['email']
        associated_users = User.objects.filter(email=email)
        if associated_users.exists():
            try:
                return super().form_valid(form)
            except SMTPException:
                messages.error(
                    self.request,
                    "An error occurred while sending the email. "
                    "Please try again later."
                )
                return redirect('users:password_reset')
        else:
            messages.error(self.request, 'Email address is not registered.')
            return redirect('users:password_reset')


def password_reset_request(request):
    """
    Handle password reset request form submission.
    If POST request, validate the form and initiate password reset process.
    If GET request, display the password reset form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered template for password reset form or redirect
                      to password reset page with an error message.
    """
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            associated_users = User.objects.filter(email=email)
            if associated_users.exists():
                return CustomPasswordResetView.as_view()(request)
            else:
                messages.error(request, 'Email address is not registered.')
                return redirect('users:password_reset')
    else:
        form = PasswordResetForm()
    return render(request, "users/password_reset.html", {"form": form})
