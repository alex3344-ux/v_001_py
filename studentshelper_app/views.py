from django.shortcuts import render
from students.models import Student


# Create your views here.

def show_studentshelper(request) -> render:
    template_ = 'studentshelper.html'

    # physics = Student.objects.filter(on_subject='Физика')
    # mathematics = Student.objects.filter(on_subject='Высшая математика')
    # informationtechnologies = Student.objects.filter(on_subject='Информационные технологии')
    # philosophy = Student.objects.filter(on_subject='Философия')

    # physics = Student.objects.select_related('Физика')
    # mathematics = Student.objects.select_related('Высшая математика')
    # informationtechnologies = Student.objects.select_related('Информационные технологии')
    # philosophy = Student.objects.select_related('Философия')

    physics = Student.objects.filter(pk=2)
    mathematics = Student.objects.filter(pk=4)
    informationtechnologies = Student.objects.filter(pk=5)
    philosophy = Student.objects.filter(pk=3)

    context = {
        'physics': physics,
        'mathematics': mathematics,
        'informationtechnologies': informationtechnologies,
        'philosophy': philosophy,
    }

    return render(request=request, template_name=template_, context=context)


