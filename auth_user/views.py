from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .models import CustomUser


def login_view(request):
    if request.method == 'POST':
        registration_no = request.POST.get('registration_no')
        password = request.POST.get('password')
        user = authenticate(request, username=registration_no, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        return render(request, 'login.html', {'error': 'Invalid registration number or password'})
    return render(request, 'login.html')


def dashboard_view(request):
    return render(request, 'base.html')


def generate_registration_no_ajax(request):
    user_type = request.GET.get('user_type')
    if user_type not in dict(CustomUser.USER_TYPE_CHOICES):
        return JsonResponse({'error': 'Invalid user_type'}, status=400)
    dummy = CustomUser(user_type=user_type)
    reg_no = dummy.generate_registration_no()
    return JsonResponse({'registration_no': reg_no})
