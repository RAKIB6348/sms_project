from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect, render

from .models import Section, Subject


def subject_list(request):
    subjects = Subject.objects.all()
    search_query = request.GET.get('q', '')

    if search_query:
        subjects = subjects.filter(
            Q(name__icontains=search_query) | Q(code__icontains=search_query)
        )

    context = {
        'subjects': subjects,
        'search_query': search_query,
    }
    return render(request, 'academic/subject/subject_list.html', context)


def subject_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        code = request.POST.get('code')

        if Subject.objects.filter(code=code).exists():
            messages.error(request, 'Subject code already exists.')
            return render(request, 'academic/subject/add-subject.html', {'form_data': {'name': name, 'code': code}})

        Subject.objects.create(name=name, code=code)
        messages.success(request, 'Subject added successfully.')
        return redirect('subject_list')

    return render(request, 'academic/subject/add-subject.html')


def subject_edit(request, pk):
    subject = Subject.objects.get(pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        code = request.POST.get('code')

        if Subject.objects.filter(code=code).exclude(pk=pk).exists():
            messages.error(request, 'Subject code already exists.')
            return render(request, 'academic/subject/edit-subject.html', {'subject': subject, 'form_data': {'name': name, 'code': code}})

        subject.name = name
        subject.code = code
        subject.save()
        messages.success(request, 'Subject updated successfully.')
        return redirect('subject_list')

    return render(request, 'academic/subject/edit-subject.html', {'subject': subject})


def subject_delete(request, pk):
    subject = Subject.objects.get(pk=pk)
    subject.delete()
    messages.success(request, 'Subject deleted successfully.')
    return redirect('subject_list')


# Section Views
def section_list(request):
    sections = Section.objects.all()
    search_query = request.GET.get('q', '')

    if search_query:
        sections = sections.filter(name__icontains=search_query)

    context = {
        'sections': sections,
        'search_query': search_query,
    }
    return render(request, 'academic/section/section_list.html', context)


def section_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Section.objects.create(name=name)
        messages.success(request, 'Section added successfully.')
        return redirect('section_list')

    return render(request, 'academic/section/add-section.html')


def section_edit(request, pk):
    section = Section.objects.get(pk=pk)
    if request.method == 'POST':
        section.name = request.POST.get('name')
        section.save()
        messages.success(request, 'Section updated successfully.')
        return redirect('section_list')

    return render(request, 'academic/section/edit-section.html', {'section': section})


def section_delete(request, pk):
    section = Section.objects.get(pk=pk)
    section.delete()
    messages.success(request, 'Section deleted successfully.')
    return redirect('section_list')
