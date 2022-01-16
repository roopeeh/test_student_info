import imp
from requests.exceptions import MissingSchema
from multiprocessing import context
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, View
from .models import StudentInfo, StudentAcademics
from student_app.models import StudentAcademics, StudentInfo
from .forms import CreateStudentForm, UpdateAccadamicsForm
from .extractor_url import extract_all_links


class StudentListView(ListView):
    """
    List of all Students with ListView from genarics
    """
    model = StudentInfo
    template_name = "home.html"


class StudentDetailsView(View):
    """
    Student Detail views GETs details of each student with Primary key 
    """

    def get(self, request, pk):

        try:

            # gets student with pk
            student = StudentInfo.objects.get(pk=pk)
            # gets Studnet accadamins object with student
            student_marks = StudentAcademics.objects.get(Student=student)

            context = {
                "name": student.Name,
                "Roll_number": student.Roll_no,
                "Maths": student_marks.Maths,
                "Physics": student_marks.Physics,
                "Chemistry": student_marks.Chemistry,
                "Biology": student_marks.Biology,
                "English": student_marks.English

            }

            return render(request, "student_details.html", context=context)

        except (TypeError, StudentInfo.DoesNotExist, StudentAcademics.DoesNotExist) as e:
            return HttpResponse("Student Details are not available")


class CreteStudent(View):

    def get(self, request):
        context = {'form': CreateStudentForm()}
        return render(request, 'create_student.html', context)

    def post(self, request):
        form = CreateStudentForm(request.POST)
        student = form.save()
        return redirect('update_marks', student.pk)


def UpdateStudentAccadamics(request, pk):
    try:
        student = StudentInfo.objects.get(pk=pk)
        student_accadamics = StudentAcademics.objects.get(Student=student)

        form_data = UpdateAccadamicsForm(
            request.POST or None, instance=student_accadamics)

        if form_data.is_valid():
            form_data.save()
            return redirect('student_list')

        context = {'form': form_data}
        return render(request, 'update_student.html', context)

    except StudentAcademics.DoesNotExist:
        # creates student accadamics object if does not exist

        student = StudentInfo.objects.get(pk=pk)
        student_accadamics = StudentAcademics()
        student_accadamics.Student = student
        student_accadamics.save()
        return redirect('update_marks', pk)


def DeleteStudent(request, pk):
    student = StudentInfo.objects.get(pk=pk)
    student.delete()
    return redirect('student_list')


class UrlExtractor(View):
    """
    This view popukates all available links for  a given url by using "extractor_url.py"
    """

    def get(self, request):

        context = {}
        context['ex'] = 'ex: https://www.google.com/'
        return render(request, "url_exreactor.html", context)

    def post(self, request):

        try:
            context = {}
            context['ex'] = request.POST['link']
            link = request.POST['link']
            context['links'] = link
            # gets all urls from the given link
            all_links = extract_all_links(link)
            http_links = []
            # filtering urls starts with Http and Https to "http_links"
            for l in all_links:
                if l.startswith('http'):
                    http_links.append(l)

            context['links'] = http_links

            return render(request, 'url_exreactor.html', context)
        except MissingSchema:
            context = {}
            context['error'] = ' Please give valid URL - Ex: https://www.google.com/'
            context['ex'] = 'ex: https://www.google.com/'
            return render(request, 'url_exreactor.html', context)
