from django.shortcuts import render
from .models import Records
from django.http import HttpResponse
from .forms import Record_form


# Create your views here.
def index(request):
    return render(request,"index.html")

def placement_list(request):
    list = Records.objects.all()
    return render(request, "placement.html", {'datas': list})


def placement_form(request):
    context = {}
    form = Record_form(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request,"placement_form.html",context)