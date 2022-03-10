from django.shortcuts import render

# Create your views here.

def index(request):
    "这是一个尺码通主页"
    return render(request,'index.html')