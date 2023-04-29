from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('webbase:index')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('webbase:index')

class SignupForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=30)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already in use')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken')
        return username


class SignupView(TemplateView):
    template_name = 'accounts/signup.html'
    form_class = SignupForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')

        if form.is_valid():
            # Get the cleaned form data
            password = form.cleaned_data.get('password1')

            
            # Create a new User object with the cleaned form data
            user = User.objects.create_user(username=username, email=email, password=password)

            # Authenticate and log the user in
            user = authenticate(request, username=username, password=password)
            login(request, user)

            return redirect('webbase:index')
        else:
            # Check if email or username already exists
            if User.objects.filter(email=email).exists() and User.objects.filter(username=username).exists():
                error_message = 'mail y usuario ya estan registrados'
            elif User.objects.filter(username=username).exists():
                    error_message = 'El usuario ya existe'
            elif User.objects.filter(email=email).exists():
                    error_message = 'El mail ya esta registrado'
            else:
                error_message = 'There was an error in the form. Please correct it.'
            messages.error(request, error_message)
            return render(request, self.template_name, {'form': form, 'error_message': error_message})
