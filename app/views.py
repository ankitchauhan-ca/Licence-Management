# licenses/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from .models import License
from django.contrib.auth.forms import AuthenticationForm
import uuid
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def base(request):
    return render(request, 'licenses/base.html')

@login_required
def create_license(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        expiration_date = request.POST.get('expiration_date')
        license_key = str(uuid.uuid4())
        License.objects.create(key=license_key, user_email=email, expiration_date=expiration_date)
        return redirect('license_list')
    return render(request, 'licenses/create_license.html')

@login_required
def license_list(request):
    licenses = License.objects.all()
    return render(request, 'licenses/license_list.html', {'licenses': licenses})

def revoke_license(request, key):
    if request.method == 'POST':
        try:
            license = License.objects.get(key=key)
            license.is_revoked = True  # Set the license as revoked
            license.save()
            return JsonResponse({'status': 'revoked'})
        except License.DoesNotExist:
            return JsonResponse({'error': 'License not found'}, status=404)

def validate_license(request, key):
    try:
        license = License.objects.get(key=key)
        return JsonResponse({'valid': license.is_valid()})
    except License.DoesNotExist:
        return JsonResponse({'valid': False, 'error': 'License not found.'})

def revoke_license(request, key):
    try:
        license = License.objects.get(key=key)
        license.is_revoked = True
        license.save()
        return JsonResponse({'status': 'revoked'})
    except License.DoesNotExist:
        return JsonResponse({'error': 'License not found.'})
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('license_list')
    else:
        form = UserCreationForm()
    return render(request, 'licenses/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('license_list')
    else:
        form = AuthenticationForm()
    return render(request, 'licenses/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

