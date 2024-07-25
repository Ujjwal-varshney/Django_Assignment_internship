from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import View
from .forms import SignUpForm, PasswordChangingForm

class SignUpView(View):
    form_class = SignUpForm
    template_name = 'signup.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
        return render(request, self.template_name, {'form': form})

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        print(f"Trying to authenticate user: {username}")  # Debug statement
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("Authentication successful")  # Debug statement
            login(request, user)
            next_url = request.GET.get('next', 'dashboard')
            return redirect(next_url)
        else:
            print("Authentication failed")  # Debug statement
            return render(request, self.template_name, {'error': 'Invalid credentials'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

@method_decorator(login_required, name='dispatch')
class DashboardView(View):
    template_name = 'dashboard.html'

    def get(self, request):
        return render(request, self.template_name)

@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    template_name = 'profile.html'

    def get(self, request):
        return render(request, self.template_name)

class CustomPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('dashboard')
    template_name = 'change_password.html'
