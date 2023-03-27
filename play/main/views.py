from django.shortcuts import render, redirect

from .forms import *


def begin(request):
    return render(request, 'main/begin.html')


def main(request):
    return render(request, 'main/main.html')


def play(request):
    return render(request, 'main/play.html')


def training(request):
    return render(request, 'main/training.html')


def career(request):
    return render(request, 'main/career.html')

def create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
           #print(form.cleaned_data)
            form.save()
            return redirect('main')

    else:
        form = PersonForm()
    return render(request, 'main/create.html', {'form': form})