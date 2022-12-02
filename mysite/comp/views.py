from django.shortcuts import render


def index(request):
    return render(request, 'comp/index.html')


def about(request):
    return render(request, 'comp/about.html')


def site_help(request):
    return render(request, 'comp/help.html')