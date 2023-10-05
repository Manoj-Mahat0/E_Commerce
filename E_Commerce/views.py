from django.shortcuts import redirect,render
from app.models import slider

def BASE(request):
    return render(request,'base.html')


def HOME(request):
    sliders = slider.objects.all()
    context ={
        'sliders':sliders,
    }
    return render(request,'main/home.html',context)