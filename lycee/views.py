from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView

from lycee.forms import StudentForm, PresenceForm
from .models import Cursus, Student, Presence


# Create your views here.


def detail(request, cursus_id):
    c = Cursus.objects.get(pk=cursus_id)
    students = c.student_set.all()
    result_list = {}
    for s in students:
        result_list[s.id] = s.first_name + " " + s.last_name

    context = {'liste': result_list}

    return render(request, 'lycee/cursus/detail_cursus.html', context)


def index(request):
    result_list = Cursus.objects.order_by('name')
    # template = loader.get_template('lycee/index.html')

    context = {
        'liste': result_list,
    }

    # return HttpResponse(template.render(context, request))

    return render(request, 'lycee/index.html', context)


def detail_student(request, student_id):
    result_list = Student.objects.get(pk=student_id)

    context = {'liste': result_list}

    return render(request, 'lycee/student/detail_student.html', context)


def update_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    form = None

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('detail_student', student_id)
    else:
        form = StudentForm(instance=student)

    return render(request, 'lycee/student/update_student.html', {'form': form})


class StudentCreateView(CreateView):
    model = Student

    form_class = StudentForm

    template_name = 'lycee/student/create.html'

    def get_success_url(self):
        return reverse("detail_student", args=(self.object.pk,))


class PresenceCreateView(CreateView):
    model = Presence

    form_class = PresenceForm

    template_name = 'lycee/presence/create.html'

    def get_success_url(self):
        return reverse("detail_presence", args=(self.object.pk,))


def call_of_role(request, cursus_id):
    if request.method == "POST":
        for s in request.POST.getlist('missing'):
            date = request.POST.getlist('date_cursus_call')
            str_date = "".join(date)

            new_missing = Presence(
                dateOfCall=str_date,
                reason="Missing",
                isMissing=True,
                student=Student.objects.get(pk=s)
            )

            new_missing.save()
        return redirect('detail_all_presence')

    c = Cursus.objects.get(pk=cursus_id)
    students = c.student_set.all()
    result_list = {}
    for s in students:
        result_list[s.id] = s.first_name + " " + s.last_name

    context = {'liste': result_list}

    return render(request, 'lycee/cursus_call/detail_cursus_call.html', context)


def detail_presence(request, presence_id):
    result_list = Presence.objects.get(pk=presence_id)

    context = {'liste': result_list}

    return render(request, 'lycee/presence/detail_presence.html', context)


def detail_all_presence(request):
    result_list = Presence.objects.all().order_by('student__last_name')
    cursus = Cursus.objects.all()

    context = {'cursus': cursus, 'presence': result_list}

    return render(request, 'lycee/presence/call_of_roll.html', context)


def particualar_call_of_role(request, student_id):
    student = Student.objects.get(pk=student_id)

    return render(request, 'lycee/presence/call_of_roll.html')


