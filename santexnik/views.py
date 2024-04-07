from django import views
from django.shortcuts import render
from .models import Santexnik
from .forms import SantexnikForm
from django.http import HttpResponse
from django.template import loader


def santexnik_list(request):
    santexnik = Santexnik.objects.all()
    form = SantexnikForm()

    context = {'santexnik': santexnik, 'form': form}
    template = loader.get_template('santexnik/santexnik_list.html')
    html_content = template.render(context)

    response = HttpResponse(html_content, content_type='text/html')

    return response

def add_santexnik(request):
    form = SantexnikForm()
    if request.method == 'POST':
        form = SantexnikForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'santexnik/add_santexnik.html', {'form': form})


def edit_santexnik(request, pk):
    santexnik = Santexnik.objects.get(id=pk)
    form = SantexnikForm(instance=santexnik)
    if request.method == 'POST':
        form = SantexnikForm(request.POST, instance=santexnik)
        if form.is_valid():
            form.save()
    return render(request, 'santexnik/edit_santexnik.html', {'form': form})

def delete_santexnik(request, pk):
    santexnik = Santexnik.objects.get(id=pk)
    santexnik.delete()
    return render(request, 'santexnik/delete_santexnik.html', {'santexnik': santexnik})