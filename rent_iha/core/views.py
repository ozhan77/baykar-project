from django.shortcuts import render
from iha.models import Category, iha
# Create your views here.
def index(request):
    ihas=iha.objects.filter(isrented=False)[0:6]
    categories = Category.objects.all()

    return render(request,'core/index.html',
    {
        'categories':categories,
        'ihas':ihas,
    })

def contact(request):
    return render(request,'core/contact.html')