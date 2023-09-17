from django.shortcuts import render, get_object_or_404
from .models import iha
# Create your views here.
def detail(request, pk):
    iha = get_object_or_404(iha,pk=pk)
    return render(request,'iha/detail.html',{
        'iha':iha
    })