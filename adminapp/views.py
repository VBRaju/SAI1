from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from .models import About_Us, Team_Members


# Home page
def home(request):
    return render(request, "base.html", {})


# About page
def about(request):
    objs = About_Us.objects.all()
    return render(request, "about.html", {'objs': objs})


# team page
def team(request):
    objs = Team_Members.objects.all()
    return render(request, "team.html", {'objs': objs})



# def about(request):
#     return render(request, 'about.html', {})


# def about_us(request, slug):
#     print(slug)
#     obj=About_Us.objects.all()
#     return render_to_response('about_us.html', {
#         'About_Us': get_object_or_404(About_Us, slug=slug),
#         'obj': obj
#     })



