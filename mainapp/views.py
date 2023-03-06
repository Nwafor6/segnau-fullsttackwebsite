from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Blog, Newsletter
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

class HomePageView(TemplateView):
    template_name="mainapp/index.html"

class AboutPageView(TemplateView):
    template_name="mainapp/about.html"

class BlogsPageView(ListView):
    template_name="mainapp/blog.html"
    model=Blog
    context_object_name="blogs"

class BlogDetailPageView(DetailView):
    template_name="mainapp/blog-single.html"
    model=Blog
    context_object_name="blog"

class ContactPageView(TemplateView):
    template_name="mainapp/contact.html"

@csrf_exempt
def Subscribe(request):
    if request.method=="POST":
        email=request.POST["email"]
        try:
            Newsletter.objects.create(email=email)
        except:
            return JsonResponse({"detail":"Already a subscriber !!"})
    return JsonResponse({"detail":"Thank you for subscribing."})
    