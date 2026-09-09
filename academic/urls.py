from django.urls import path

from . import views

urlpatterns = [
    # Subject URLs
    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/add/', views.subject_add, name='subject_add'),
    path('subjects/edit/<int:pk>/', views.subject_edit, name='subject_edit'),
    path('subjects/delete/<int:pk>/', views.subject_delete, name='subject_delete'),

    # Section URLs
    path('sections/', views.section_list, name='section_list'),
    path('sections/add/', views.section_add, name='section_add'),
    path('sections/edit/<int:pk>/', views.section_edit, name='section_edit'),
    path('sections/delete/<int:pk>/', views.section_delete, name='section_delete'),

    # Academic Year URLs
    path('academic-years/', views.academic_year_list, name='academic_year_list'),
    path('academic-years/add/', views.academic_year_add, name='academic_year_add'),
    path('academic-years/edit/<int:pk>/', views.academic_year_edit, name='academic_year_edit'),
    path('academic-years/delete/<int:pk>/', views.academic_year_delete, name='academic_year_delete'),
]
