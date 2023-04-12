from django.http import HttpResponse
from django.shortcuts import render
def demo(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def java(request):
    return render(request,'javascript.html')
# Create your views here.
