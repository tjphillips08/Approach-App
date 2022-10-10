from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Course
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"


class About(TemplateView):
    template_name = "about.html"


class CourseList(TemplateView):
    template_name = "course_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mySearchName = self.request.GET.get("name")
        if mySearchName != None:
            context["courses"] = Course.objects.filter(name__icontains=mySearchName)
            context["stuff_at_top"] = f"Searching for {mySearchName}"
        else:
            context["courses"] = Course.objects.all()
            context["stuff_at_top"] = "All Courses"
            return context


class CourseCreate(CreateView):
    model = Course
    fields = ['name', 'img', 'address', 'website']
    template_name = "course_create.html"
    def get_success_url(self):
        return reverse('course_detail', kwargs={'pk': self.object.pk})


class CourseDetail(DetailView):
    model = Course
    template_name = "course_detail.html"


class CourseUpdate(UpdateView):
    model = Course
    fields = ['name', 'img', 'address', 'website']
    template_name = "course_update.html"
    def get_success_url(self):
        return reverse('course_detail', kwargs={'pk': self.object.pk})



class CourseDelete(DeleteView):
    model = Course
    template_name = "course_delete_confirmation.html"
    success_url = "/courses/"
    
        