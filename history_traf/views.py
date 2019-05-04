from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'history_traf/history_traf.html')
