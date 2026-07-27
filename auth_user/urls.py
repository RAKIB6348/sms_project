from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('ajax/generate-registration-no/', views.generate_registration_no_ajax, name='generate_registration_no'),
]
