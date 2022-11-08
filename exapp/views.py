from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.views.generic.edit import UpdateView
from django.views.generic import DetailView
from stdapp.models import Student,CheckPoint
# Create your views here.
from exapp.models import Course
from exapp.forms import SeachForm,CourseForm
def index(request):

    course_list = Course.objects.all()
    form = SeachForm(request.GET)
    if form.is_valid():
        search =form.cleaned_data['search']
        course_list = course_list.filter(name__icontains=search)
    context = {
        'course_list':course_list,
        'form':form,
    }
    return render(request,'exapp/course_list.html',context)

class CourseDetail(DetailView):
    model =Course

class CourseUpdate(UpdateView):
    model =Course
    form_class= CourseForm


def course_form(request,pk):
    course = Course.objects.get(id=pk)
    if not  request.user.is_authenticated:
        return redirect(course.get_absolute_url())
    if request.method == "POST":
        form = CourseForm(request.POST,instance=course)

        perm = request.user.has_perm('exapp.change_course')
        if perm and form.is_valid() :
            form.save()
            return redirect(course.get_absolute_url())
    else:
        form = CourseForm(instance=course)

    context = {
        'course':course,
        'form':form,
    }
    return render(request,'exapp/course_form.html',context)

def course_detail(request,pk):
    course = Course.objects.get(id=pk)
    exersise_list = course.exersise_set.all()

    student_set =  Student.objects.filter(checkpoint__exersise__course__id=course.id).distinct()
    student_list =[]

    for x in student_set:
        tmp = [x.name]
        for e in exersise_list:
            checkpoint = CheckPoint.objects.filter(student=x,exersise=e)
            if checkpoint.exists():
                tmp.append(checkpoint[0].status)
            else:
                tmp.append('')
        student_list.append(tmp)

    context = {
        'course':course,
        'exersise_list':exersise_list,
        'student_list':student_list
    }
    return render(request,'exapp/course_detail.html',context)
