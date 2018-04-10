from django.shortcuts import render

def index(request):
    return render(request, 'myadmin/index.html')
