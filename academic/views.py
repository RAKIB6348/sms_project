from django.contrib import messages
from django.shortcuts import redirect, render

from .models import Subject


# TODO: Create subject list template and implement full list view
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'academic/subject/subject_list.html', {'subjects': subjects})


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
