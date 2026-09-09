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
