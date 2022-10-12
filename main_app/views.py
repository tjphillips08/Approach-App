from django.shortcuts import get_object_or_404, render
from django.views import View 
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Course, Member, Club, Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.shortcuts import redirect
from django.views import generic
from .forms import CommentForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clubs"] = Club.objects.all()
        return context


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



class MemberCreate(CreateView):
    def post(self, request, pk):
        name = request.POST.get("name")
        handicap = request.POST.get("handicap")
        email = request.POST.get("email")
        course = Course.objects.get(pk=pk)
        Member.objects.create(name=name, handicap=handicap, email=email, course=course)
        return redirect('course_detail', pk=pk)



class ClubList(TemplateView):
    template_name = "club_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ["clubs"] = Club.objects.all()
        return context



class ClubMemberAssoc(View):
    def get(self, request,pk, member_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Club.objects.get(pk=pk).members.remove(member_pk)
        if assoc =="add":
            Club.objects.get(pk=pk).members.add(member_pk)
        return redirect('/clubs/')



class ClubDetail(DetailView):
    model = Club
    template_name = "club_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clubs"] = Club.objects.all()
        return context



class ClubCreate(CreateView):
    model = Club
    fields = ['name', 'img', 'members']
    template_name = "club_create.html"
    def get_success_url(self):
        return reverse('club_detail', kwargs={'pk': self.object.pk})



@method_decorator(login_required, name='dispatch')
class PostList(generic.ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name = "post_list.html"
    paginate_by = 3



def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

    else:
        comment_form = CommentForm()

    return render(request, template_name, {"post": post, "comments": comments, "new_comment": new_comment, "comment_form": comment_form})



class PostCreate(CreateView):
    model = Post
    fields = ['title', 'author', 'content']
    template_name = "post_create.html"
    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug': str(self.slug)})



class Signup(View):
    
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("course_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)


  
   



        












    
        