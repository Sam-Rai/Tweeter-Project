from django.shortcuts import render


from django.http import HttpResponse

def myhome(request):
    return render(request, 'index.html')