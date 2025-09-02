from django.shortcuts import render

def projectpage(request):
    return render(request, 'index.html')