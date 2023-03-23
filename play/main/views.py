from django.shortcuts import render


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